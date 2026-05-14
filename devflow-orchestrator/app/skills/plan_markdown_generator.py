from datetime import datetime


def generate_markdown_plan(issue_title, issue_number, context, plan):

    markdown = f"""
# Development Plan - Issue #{issue_number}

## Issue

{issue_title}

---

## Generated At

{datetime.utcnow().isoformat()} UTC

---

# Project Context

| Property | Value |
|---|---|
| Repository | {context.repository} |
| Language | {context.language} |
| Framework | {context.framework} |
| Build Tool | {context.build_tool} |
| Java Version | {context.java_version} |

---

# Dependencies

"""

    for dependency in context.dependencies:
        markdown += f"- {dependency}\n"

    markdown += "\n---\n"
    markdown += "\n# Planned Steps\n\n"

    steps = plan.get("steps", [])

    for step in steps:

        markdown += f"""
## Step {step.get("id")}

### Type
{step.get("type")}

### Description
{step.get("description")}

---
"""

    markdown += """

# Approval

- [ ] Approved
- [ ] Rejected

"""

    return markdown