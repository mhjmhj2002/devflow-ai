# app/api/webhook.py

from fastapi import APIRouter, Header

from app.core.logger import logger
from app.schemas.github import GitHubWebhookPayload
from app.github.normalizer import normalize_github_event
from app.workflows.workflow_router import route_workflow

router = APIRouter()


@router.post("/webhook/github")
async def github_webhook(
        payload: GitHubWebhookPayload,
        x_github_event: str = Header(default="unknown")
):

    logger.info(f"GitHub event received: {x_github_event}")

    normalized_event = normalize_github_event(
        x_github_event,
        payload.model_dump()
    )

    logger.info(f"Normalized payload: {normalized_event}")

    result = await route_workflow(normalized_event)

    return result