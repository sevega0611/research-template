import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file automatically

# ─────────────────────────────────────────────
#  Project Configuration
#  Add your username and paths below
# ─────────────────────────────────────────────

USER = os.environ.get("USER", "")

PATHS = {
    "svegahar": {
        "github":  "/Users/svegahar/Documents/GitHub/[repo]",
        "dropbox": "/Users/svegahar/Library/CloudStorage/Dropbox/NotreDame/[ProjectFolder]",
    },
    # Add collaborators below:
    # "collaborator": {
    #     "github":  "/Users/collaborator/Documents/GitHub/[repo]",
    #     "dropbox": "/Users/collaborator/Dropbox/NotreDame/[ProjectFolder]",
    # },
}

if USER not in PATHS:
    raise ValueError(
        f"User '{USER}' not found in config.py. "
        "Please add your username and paths to the PATHS dictionary."
    )

# ─────────────────────────────────────────────
#  Root paths
# ─────────────────────────────────────────────
github  = PATHS[USER]["github"]
dropbox = PATHS[USER]["dropbox"]

# ─────────────────────────────────────────────
#  Data paths (Dropbox)
# ─────────────────────────────────────────────
raw   = os.path.join(dropbox, "raw")
clean = os.path.join(dropbox, "clean")

# Add source-specific paths below:
# raw_source1   = os.path.join(raw, "source1")
# clean_source1 = os.path.join(clean, "source1")

# ─────────────────────────────────────────────
#  API Keys (loaded from .env)
# ─────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Add other keys as needed:
# OTHER_API_KEY = os.getenv("OTHER_API_KEY")


# ─────────────────────────────────────────────
#  Quick test
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(f"User:    {USER}")
    print(f"GitHub:  {github}")
    print(f"Dropbox: {dropbox}")
    print(f"Raw:     {raw}")
    print(f"Clean:   {clean}")
    print("config.py loaded successfully.")
