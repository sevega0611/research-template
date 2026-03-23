# Claude Context: Sebastián Vega Haro

## Who I Am

I am a pre-doctoral research assistant at the University of Notre Dame, working on empirical economics research focused on econometrics, causal inference, and public finance. I am responsible for the full paper pipeline: data collection, cleaning, analysis, and writing.

## My Primary Work

- Build and manage data pipelines for empirical economics research
- Web scraping and LLM-based text processing for large-scale datasets
- Econometric analysis and causal inference
- Academic writing (paper + policy briefs)

## Tools and Software

| Tool | What I Use It For | Where Files Live |
|------|-------------------|------------------|
| Python | Web scraping, LLM batch processing, data cleaning | GitHub: `code/build/` |
| Jupyter Notebooks | Development and exploration | GitHub: `code/build/*/notebooks/` |
| Stata | Econometric analysis | GitHub: `code/analysis/` |
| LaTeX | Paper writing | GitHub: `paper/` |
| GitHub | Version control, task tracking (Issues) | github.com/[org]/[repo] |
| Dropbox | Raw and clean data storage | `~/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]/` |

## Where My Files Are Stored

- **Code:** `~/Documents/GitHub/[repo]/`
- **Raw data:** `~/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]/raw/`
- **Clean data:** `~/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]/clean/`
- **Literature:** `~/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]/literature/`
- **All paths are managed via `config.py`** — never hardcode paths in scripts

## How I Prefer to Work

- Explain what you are going to do before doing it
- Ask before modifying or moving files
- Be concise unless I ask for detail
- Communicate in Spanish unless I write in English
- Always use `config.py` for paths and API keys — never hardcode them

## Skill Level

- **Python:** Advanced (web scraping, APIs, LLM batch processing)
- **Stata:** Advanced (econometrics, causal inference)
- **R:** Advanced
- **Statistics:** Advanced (causal inference, RDD, DID, IV)
- **Git/GitHub:** Intermediate
- **Command line:** Intermediate

---

# Project: [PROJECT_TITLE]

## Research Question

[Describe the main research question and identification strategy.]

## Team

| Person | Role |
|--------|------|
| [PI Name] (Notre Dame) | Principal Investigator |
| Sebastián Vega Haro (Notre Dame) | Lead RA — code and writing |

## Data Sources

| # | Source | Coverage | Status |
|---|--------|----------|--------|
| 01 | [Source 1] | [Coverage] | [Status] |
| 02 | [Source 2] | [Coverage] | [Status] |

## Pipeline

```
code/build/
├── 01_[source1]/     → clean/[source1]/
└── 02_[source2]/     → clean/[source2]/

code/analysis/        → output/
```

Run everything with: `python 00_master.py`

## Code Conventions

- **Always** import `config.py` at the top of every script
- **Never** hardcode paths or API keys
- Raw data goes in `raw/` — never modify raw files
- Processed data goes in `clean/`
- Notebooks for exploration go in `*/notebooks/` — final scripts are `.py`

```python
# Standard header for every script
import sys
sys.path.insert(0, "/Users/yourusername/Documents/GitHub/[repo]")
from config import github, dropbox, raw, clean
```

## Key Decisions

| Decision | Reason |
|----------|--------|
| [Decision 1] | [Reason] |
| [Decision 2] | [Reason] |

## Open Issues

Check live issues with `/issues` or at: github.com/[org]/[repo]/issues

---

# Custom Skills

All custom commands live in `.claude/commands/`. Use them at any time:

| Command | Description |
|---------|-------------|
| `/summary` | Weekly progress summary |
| `/status` | Status of all data sources |
| `/pipeline` | Full pipeline walkthrough |
| `/issues` | List all open GitHub issues |
| `/issue [N]` | Detail of issue N |
| `/close-issue [N]` | Close issue N |
| `/comment-issue [N]` | Add comment to issue N |
| `/check-data` | Verify datasets integrity |
| `/check-notebooks` | List notebooks and flag issues |
| `/papers` | List literature folder |
| `/report` | Generate daily progress report |
| `/commit [msg]` | Stage, commit, and push |
| `/setup` | Onboarding for new machine |

---

# Onboarding: New Collaborator Setup

1. Clone the repo:
```bash
git clone https://github.com/[org]/[repo].git
cd [repo]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your paths to `config.py`:
```python
"yourusername": {
    "github":  "/Users/yourusername/Documents/GitHub/[repo]",
    "dropbox": "/Users/yourusername/Dropbox/NotreDame/[ProjectFolder]",
}
```

4. Create your `.env` file:
```bash
cp .env.example .env
# Open .env and add your API keys
```

5. Make sure you have access to the shared Dropbox folder.

6. Run `/setup` in Claude Code if you need help.
