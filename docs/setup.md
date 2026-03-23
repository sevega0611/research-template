# Project Setup Guide
**[PROJECT_TITLE]**

This guide walks a new collaborator through the complete setup. Follow the steps for your operating system.

---

## Requirements

- A computer with internet access
- Access to the shared Dropbox folder: `NotreDame/[ProjectFolder]/`
- A GitHub account with access to `github.com/[org]/[repo]`
- API keys (ask Sebastián)

---

## Step 1 — Install Git

**Mac:**
```bash
git --version
```
If not installed, macOS will prompt you to install it automatically.

**Windows:**
Download and install from: https://git-scm.com/download/win

During installation, select:
- "Use Git from the Windows Command Prompt"
- "Checkout Windows-style, commit Unix-style line endings"

After installation, use **Git Bash** for all terminal commands.

---

## Step 2 — Configure Git Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## Step 3 — Install Homebrew (Mac only)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile && eval "$(/opt/homebrew/bin/brew shellenv)"
```

---

## Step 4 — Install GitHub CLI

**Mac:**
```bash
brew install gh
```

**Windows:**
Download from: https://cli.github.com/

---

## Step 5 — Authenticate with GitHub

```bash
gh auth login
```

Select: `GitHub.com` → `HTTPS` → `Login with a web browser`

---

## Step 6 — Install Python

**Mac:**
```bash
python3 --version   # check if installed
brew install python # if not
```

**Windows:**
Download from https://www.python.org/downloads/ — check **"Add Python to PATH"** during install.

---

## Step 7 — Clone the Repository

**Mac:**
```bash
cd ~/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]
git clone https://github.com/[org]/[repo].git [repo]
cd [repo]
```

**Windows (Git Bash):**
```bash
cd ~/Dropbox/NotreDame/[ProjectFolder]
git clone https://github.com/[org]/[repo].git [repo]
cd [repo]
```

---

## Step 8 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 9 — Add Your Paths to `config.py`

Open `config.py` and add your entry to the `PATHS` dictionary.

**Mac:**
```python
"yourusername": {
    "github":  "/Users/yourusername/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]/[repo]",
    "dropbox": "/Users/yourusername/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]",
},
```

**Windows:**
```python
"yourusername": {
    "github":  "C:/Users/yourusername/Dropbox/NotreDame/[ProjectFolder]/[repo]",
    "dropbox": "C:/Users/yourusername/Dropbox/NotreDame/[ProjectFolder]",
},
```

Find your username:
- Mac: `echo $USER`
- Windows (Git Bash): `echo $USERNAME`

---

## Step 10 — Set Up API Keys

```bash
cp .env.example .env
```

Open `.env` and fill in your keys. **Never commit this file.**

---

## Step 11 — Verify Dropbox Sync

Make sure these folders exist and are synced:

```
NotreDame/[ProjectFolder]/
├── raw/
├── clean/
└── literature/
```

---

## Step 12 — Test Your Setup

```bash
python config.py
```

No errors = you are ready.

---

## Daily Workflow

**Before starting — pull latest changes:**
```bash
git pull
```

**After finishing — save and share:**
```bash
git add .
git commit -m "brief description"
git push
```

Or use `/commit` in Claude Code.

---

## Using Claude Code (Optional but recommended)

Claude Code is an AI assistant with full project context.

**Install:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Start inside the project folder:**
```bash
cd ~/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]/[repo]  # Mac
claude
```

Available commands: `/summary`, `/status`, `/pipeline`, `/issues`, `/report`, `/commit`, `/setup`

---

## Getting Help

- Read `CLAUDE.md` for full project documentation
- Open a GitHub issue if something is broken
- Contact Sebastián Vega Haro for setup questions
