"""Simple code generation orchestrator (MVP).

This module demonstrates a safe, minimal code generation workflow:
- Determine project path
- Create a branch named `devflow/issue-<n>-generated`
- Write a small marker file under the target service
- Commit and push

This is intentionally minimal; it will not perform arbitrary deletions
and it operates only inside the target service directory.
"""

from pathlib import Path
from typing import Dict, Any
from app.core.logger import logger
from app.project_context.context_registry import get_project_path
from app.git.git_client import GitClient
import hashlib
import re
from app.github.pr_creator import create_pull_request
from app.github.github_commenter import post_github_comment


def _slugify(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:40]


def start_codegen_workflow(payload: Dict[str, Any]):
    """Start a minimal code generation workflow.

    payload expected keys: repository, issue_number, comment
    """
    repository = payload.get("repository")
    issue_number = payload.get("issue_number") or "0"
    comment = payload.get("comment") or {}

    logger.info(f"Starting codegen for repo={repository} issue={issue_number}")

    repo_path = get_project_path(repository)
    if not repo_path:
        raise RuntimeError(f"repository not mapped: {repository}")

    # Target only the repository path (sandbox)
    target = Path(repo_path)

    # create an ephemeral branch name
    title_fragment = (comment.get("body") or "generated").splitlines()[0][:50]
    slug = _slugify(title_fragment)
    branch = f"devflow/issue-{issue_number}-{slug or hashlib.md5(str(issue_number).encode()).hexdigest()[:6]}"

    git = GitClient()

    # perform checkout in-place (assumes repo already exists locally)
    # If the resolved path is not a git repo, bail out gracefully
    if not (target / ".git").exists():
        logger.warning(f"Target path is not a git repo: {target}; skipping clone/branch. Creating files locally.")

    # create a generated marker file in a safe location under the target
    gen_file = target / "devflow_ai_generated" / f"issue_{issue_number}_generated.txt"
    gen_file.parent.mkdir(parents=True, exist_ok=True)

    content = (
        f"DevFlow AI generated artifacts\nRepository: {repository}\nIssue: {issue_number}\nComment: {str(comment.get('body'))[:200]}\n"
    )

    gen_file.write_text(content)

    # attempt to commit and push if .git exists
    if (target / ".git").exists():
        code, out, err = git.checkout_new_branch(str(target), branch)
        if code != 0:
            logger.warning(f"Failed creating branch: {out} {err}")
        else:
            msg = f"chore(devflow): ai generated changes for issue {issue_number}"
            code2, out2, err2 = git.add_commit_push(str(target), msg, branch)
            if code2 != 0:
                logger.warning(f"Failed add/commit/push: {out2} {err2}")
            else:
                # attempt to create pull request if push succeeded
                try:
                    pr = create_pull_request(repository=repository, head=branch)
                    logger.info(f"PR creation result: {pr}")

                    # if PR created successfully, comment on the originating issue with the PR link
                    if isinstance(pr, dict) and pr.get("status") == "ok":
                        pr_result = pr.get("result") or {}
                        pr_url = pr_result.get("html_url") or pr_result.get("url")
                        if pr_url:
                            try:
                                post_github_comment(
                                    repository=repository,
                                    issue_number=issue_number,
                                    body=f"DevFlow: created Pull Request for generated changes: {pr_url}"
                                )
                            except Exception:
                                logger.exception("Failed to post PR link comment")
                except Exception:
                    logger.exception("Failed to create PR")

    logger.info(f"Codegen workflow finished for {repository}#{issue_number} branch={branch}")
    return {"repository": repository, "issue_number": issue_number, "branch": branch, "generated": True}

