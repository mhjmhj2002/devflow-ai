# app/workflows/workflow_router.py

from app.workflows.planning_workflow import start_planning_workflow


async def route_workflow(event: dict):

    event_type = event.get("event")
    action = event.get("action")

    # ISSUE OPENED -> start planning workflow
    if event_type == "issues" and action == "opened":
        return await start_planning_workflow(event)

    return {
        "status": "ignored",
        "reason": "event not supported"
    }