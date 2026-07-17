# Local agent implementations

Each numbered folder is an isolated Python 3.11 project. Create a virtual environment inside the
selected folder, install its requirements, copy `.env.example` to `.env`, and run `agent.py --help`
before making a provider-backed request.

## Quick start

```bash
cd agents/01-web-research-agent
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python agent.py --help
```

## Agent index

| # | Agent | Framework | Model in code | Industry | Difficulty |
|---:|---|---|---|---|---|
| 01 | [Web Research Agent](01-web-research-agent/) | LangGraph | `gpt-4o-mini` | General | Intermediate |
| 02 | [Code Review Agent](02-code-review-agent/) | LangChain | `gpt-4o` | Software development | Beginner |
| 03 | [PDF Q&A Agent](03-pdf-qa-agent/) | LlamaIndex | `gpt-4o-mini` | Research | Beginner |
| 04 | [SQL Query Agent](04-sql-query-agent/) | LangChain | `gpt-4o-mini` | Data analytics | Intermediate |
| 05 | [Email Drafting Agent](05-email-drafting-agent/) | CrewAI | `gpt-4o-mini` | Communication | Beginner |
| 06 | [News Summarizer Agent](06-news-summarizer-agent/) | LangChain | `gpt-4o-mini` | Media | Beginner |
| 07 | [GitHub Issue Triager](07-github-issue-triager/) | LangChain | `gpt-4o-mini` | Software development | Intermediate |
| 08 | [Data Analysis Agent](08-data-analysis-agent/) | LangChain | `gpt-4o` | Analytics | Intermediate |
| 09 | [Resume Parser Agent](09-resume-parser-agent/) | LangChain | `gpt-4o-mini` | Human resources | Beginner |
| 10 | [Meeting Notes Agent](10-meeting-notes-agent/) | LangChain | `gpt-4o-mini` | Productivity | Beginner |
| 11 | [Stock Research Agent](11-stock-research-agent/) | LangChain | `gpt-4o-mini` | Finance | Intermediate |
| 12 | [Travel Planner Agent](12-travel-planner-agent/) | CrewAI | `gpt-4o-mini` | Travel | Intermediate |
| 13 | [Customer Support Agent](13-customer-support-agent/) | LangGraph | `gpt-4o-mini` | Customer service | Advanced |
| 14 | [Social Media Agent](14-social-media-agent/) | CrewAI | `gpt-4o-mini` | Marketing | Beginner |
| 15 | [Unit Test Generator](15-unit-test-generator/) | LangChain | `gpt-4o` | Software development | Intermediate |
| 16 | [Documentation Writer](16-documentation-writer/) | LangChain | `gpt-4o` | Software development | Intermediate |
| 17 | [Recipe Agent](17-recipe-agent/) | LangChain | `gpt-4o-mini` | Food | Beginner |
| 18 | [Job Application Agent](18-job-application-agent/) | CrewAI | `gpt-4o-mini` | Human resources | Intermediate |
| 19 | [Competitive Analysis Agent](19-competitive-analysis-agent/) | LangGraph | `gpt-4o` | Business | Advanced |
| 20 | [Multi-Agent Debate](20-multi-agent-debate/) | LangChain | `gpt-4o` | Research | Advanced |

For categories, tags, validation status, and audit dates, use the root
[Project Index](../PROJECT_INDEX.md).

## Add an agent

Start from [`templates/agent/`](../templates/agent/) and follow
[`CONTRIBUTING.md`](../CONTRIBUTING.md). Do not copy an external project into this collection without
its required license, copyright notice, and source attribution.
