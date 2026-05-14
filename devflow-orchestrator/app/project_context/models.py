# app/project_context/models.py

from pydantic import BaseModel
from typing import List, Optional


class ProjectContext(BaseModel):
    repository: str

    language: Optional[str] = None
    framework: Optional[str] = None
    build_tool: Optional[str] = None

    java_version: Optional[str] = None

    dependencies: List[str] = []

    architecture_hints: List[str] = []

    source_directories: List[str] = []