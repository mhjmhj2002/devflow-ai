# app/project_context/context_registry.py

from pathlib import Path

PROJECTS = {
    "agentic-ms-user": "/home/mhj/git/agentic-ms-user",
    "agentic-ms-order": "/home/mhj/git/agentic-ms-order"
}


def get_project_path(repository_or_service: str):
    """
    Resolve a project path by repository name or service name.

    Strategy:
    - Check explicit PROJEC TS mapping
    - If not found, try to resolve to monorepo/services/{name} or monorepo/services/{name}-service
    - Return None if not found
    """

    if not repository_or_service:
        return None

    # 1) explicit mapping
    path = PROJECTS.get(repository_or_service)
    if path:
        return path

    # 2) try to resolve under monorepo services/
    try:
        base = Path(__file__).resolve().parents[3]  # devflow-ai

        candidate = base / "services" / repository_or_service
        if candidate.exists():
            return str(candidate)

        # try with -service suffix
        candidate2 = base / "services" / f"{repository_or_service}-service"
        if candidate2.exists():
            return str(candidate2)

    except Exception:
        pass

    return None
