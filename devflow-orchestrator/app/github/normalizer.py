from app.core.logger import logger


def normalize_github_event(event: str, payload: dict):

    logger.info(f"Normalizing GitHub event: {event}")

    repository = payload.get("repository", {}).get("name")
    issue = payload.get("issue", {}) or {}

    # try to extract service from labels (labels come as list of dicts with 'name')
    service = None
    labels = issue.get("labels") or []

    for label in labels:
        # label may be dict or simple string
        name = None
        if isinstance(label, dict):
            name = label.get("name")
        else:
            name = str(label)

        if name and name.startswith("service:"):
            # service:identity -> identity
            service = name.split(":", 1)[1].strip()
            break

    normalized = {
        "event": event,
        "action": payload.get("action"),
        "repository": repository,
        "issue_number": issue.get("number"),
        "issue_title": issue.get("title"),
        "labels": [l.get("name") if isinstance(l, dict) else str(l) for l in labels],
        "service": service
    }

    return normalized