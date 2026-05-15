# app/events/validator.py

from app.core.logger import logger
from app.events.contracts.issue_events import IssueOpenedEvent, IssueCommentCreatedEvent


class EventValidator:

    @staticmethod
    def validate(event_name: str, payload: dict):

        logger.info(f"Validating event: {event_name}")

        # Support issues and issue_comment events
        if event_name not in ("issues", "issue_comment"):
            return None, "unsupported event"

        try:
            # Support two payload shapes:
            # 1) raw GitHub payload: { repository: {name}, issue: {...} }
            # 2) normalized payload: { repository: "name", issue_number: n, issue_title: "...", labels: [...] }

            repository = payload.get("repository")
            issue = payload.get("issue")

            # handle issue_comment (GitHub raw payload):
            # payload: { repository: {...}, issue: {...}, comment: {...} }
            if event_name == "issue_comment":
                comment = payload.get("comment")
                # normalized shape possibility: repository is string, issue_number, comment_body
                if isinstance(payload.get("repository"), str) and (payload.get("issue_number") or payload.get("comment_body")):
                    repository_safe = {"name": payload.get("repository")}
                    comment_safe = {
                        "id": payload.get("comment_id") or 0,
                        "body": payload.get("comment_body"),
                        "user": {"login": payload.get("comment_user") or ""}
                    }

                    event = IssueCommentCreatedEvent(
                        repository=repository_safe,
                        issue_number=payload.get("issue_number"),
                        comment=comment_safe,
                        service=payload.get("service")
                    )

                    return event, None

                # raw payload case
                if not repository or not comment:
                    return None, "missing repository or comment"

                issue_number = payload.get("issue", {}).get("number") or payload.get("issue_number")

                comment_safe = dict(comment) if isinstance(comment, dict) else comment
                # ensure body and user exist
                comment_safe = comment_safe or {}
                comment_safe["body"] = comment_safe.get("body") or ""
                user = comment_safe.get("user") or {"login": ""}
                comment_safe["user"] = user

                repository_safe = dict(repository) if isinstance(repository, dict) else repository

                event = IssueCommentCreatedEvent(
                    repository=repository_safe,
                    issue_number=issue_number,
                    comment=comment_safe,
                    service=None
                )

                return event, None

            # detect normalized payload shape: repository is a string and issue_number/title present
            if isinstance(payload.get("repository"), str) and (payload.get("issue_number") or payload.get("issue_title")):
                # normalized payload case
                repo_name = payload.get("repository")
                repository_safe = {"name": repo_name}

                issue_safe = {
                    "number": payload.get("issue_number"),
                    "title": payload.get("issue_title"),
                    "labels": []
                }

                # normalize labels if present (could be list of strings or list of dicts)
                labels_raw = payload.get("labels") or []
                normalized_labels = []
                for l in labels_raw:
                    if isinstance(l, dict):
                        name = l.get("name")
                    else:
                        name = str(l)
                    if name:
                        normalized_labels.append({"name": name})

                issue_safe["labels"] = normalized_labels

                service = payload.get("service")

                event = IssueOpenedEvent(
                    repository=repository_safe,
                    issue=issue_safe,
                    service=service
                )

                return event, None

            # legacy/raw payload case
            if not repository or not issue:
                return None, "missing repository or issue"

            # issue['labels'] may be None (pydantic optional); normalize to empty list
            labels = issue.get("labels") or []

            service = None
            for label in labels:
                # label may be dict or string
                name = label.get("name") if isinstance(label, dict) else str(label)
                if "service:" in name:
                    parts = name.split(":", 1)
                    if len(parts) > 1:
                        service = parts[1]

            # ensure we pass non-None lists to the Pydantic model
            issue_safe = dict(issue) if isinstance(issue, dict) else issue
            issue_safe = issue_safe or {}
            issue_safe["labels"] = issue_safe.get("labels") or []

            repository_safe = dict(repository) if isinstance(repository, dict) else repository

            event = IssueOpenedEvent(
                repository=repository_safe,
                issue=issue_safe,
                service=service
            )

            return event, None

        except Exception as e:
            logger.exception(e)
            return None, str(e)

