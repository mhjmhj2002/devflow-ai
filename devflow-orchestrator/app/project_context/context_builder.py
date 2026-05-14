# app/project_context/context_builder.py

from app.project_context.scanner import scan_repository
from app.project_context.stack_detector import detect_stack


def build_project_context(repo_path: str, repository: str):

    files = scan_repository(repo_path)

    context = detect_stack(files, repository)

    return context