import os
import requests


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")


def post_github_comment(
        repository: str,
        issue_number: int,
        body: str
):

    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{repository}/issues/{issue_number}/comments"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(
        url,
        headers=headers,
        json={
            "body": body
        }
    )

    response.raise_for_status()

    return response.json()