def build_planning_prompt(issue_title: str, context):

    return f"""
You are an AI software architect.

Generate a development implementation plan for the following issue.

ISSUE:
{issue_title}

PROJECT CONTEXT:

Language:
{context.language}

Framework:
{context.framework}

Build Tool:
{context.build_tool}

Source Directories:
{context.source_directories}

Generate a concise implementation plan in JSON format.

Expected format:

{{
  "steps": [
    {{
      "id": 1,
      "type": "controller",
      "description": "Create REST controller"
    }}
  ]
}}
"""