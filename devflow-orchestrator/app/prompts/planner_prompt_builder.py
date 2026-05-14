# app/prompts/planner_prompt_builder.py

from app.project_context.models import ProjectContext


def build_planner_prompt(
        issue_title: str,
        issue_body: str,
        context: ProjectContext
):

    return f"""
Project Context:

Repository:
{context.repository}

Language:
{context.language}

Framework:
{context.framework}

Build Tool:
{context.build_tool}

Java Version:
{context.java_version}

Dependencies:
{", ".join(context.dependencies)}

Issue Title:
{issue_title}

Issue Description:
{issue_body}

Generate a structured implementation plan.
"""