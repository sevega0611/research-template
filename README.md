# [PROJECT_TITLE]

## Overview

[Brief description of the research question and empirical strategy.]

**Status:** [Data collection / Analysis / Writing]

## Team

| Name | Institution | Role |
|------|-------------|------|
| [PI Name] | University of Notre Dame | Principal Investigator |
| Sebastián Vega Haro | University of Notre Dame | Lead RA |

## Data Sources

| Source | Coverage | Status |
|--------|----------|--------|
| [Source 1] | [Coverage] | [Status] |
| [Source 2] | [Coverage] | [Status] |

## Repository Structure

```
[project_name]/
├── code/
│   ├── build/
│   │   ├── 01_[source1]/     ← [Source 1] pipeline
│   │   └── 02_[source2]/     ← [Source 2] pipeline
│   └── analysis/             ← econometric analysis
├── output/
│   ├── figures/
│   └── tables/
├── paper/                    ← LaTeX manuscript
├── reports/                  ← daily progress reports
├── .claude/commands/         ← custom Claude Code skills
├── config.py                 ← paths and API keys
├── requirements.txt          ← Python dependencies
├── .env.example              ← API key template (copy to .env)
└── CLAUDE.md                 ← project context for Claude
```

**Data** lives in Dropbox (`NotreDame/[ProjectFolder]/`), not in this repo.

## Setup

See [`docs/setup.md`](docs/setup.md) for full setup instructions (Mac and Windows).

Quick start:
```bash
git clone https://github.com/[org]/[repo].git
cd [repo]
pip install -r requirements.txt
cp .env.example .env   # add your API keys
```

Add your paths to `config.py` and you are ready.

## Task Tracking

Open issues and tasks are tracked via GitHub Issues.
