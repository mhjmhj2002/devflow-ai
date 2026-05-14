from pathlib import Path


def save_plan(issue_number: int, content: str):

    plans_dir = Path("docs/plans")

    plans_dir.mkdir(parents=True, exist_ok=True)

    file_path = plans_dir / f"issue-{issue_number}-development-plan.md"

    with open(file_path, "w") as file:
        file.write(content)

    return str(file_path)