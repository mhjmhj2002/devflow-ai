from fastapi import FastAPI
from app.api.webhook import router as webhook_router
from app.core.config import settings
from app.core.logger import logger
from app.api.context import router as context_router

app = FastAPI(
    title=settings.APP_NAME
)


@app.get("/health")
async def health():

    logger.info("Healthcheck called")

    return {
        "status": "ok"
    }


app.include_router(webhook_router)

app.include_router(context_router)

logger.info("DevFlow Orchestrator started")
