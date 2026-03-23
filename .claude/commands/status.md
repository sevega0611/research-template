Show the current status of all data sources and the pipeline.

Steps:
1. Read `CLAUDE.md` to get the list of data sources and their expected raw/clean paths.
2. Read `config.py` to get the Dropbox paths.
3. For each data source, check whether the corresponding raw/ and clean/ folders exist and are non-empty.
4. Display a status table:

| Source | Raw | Clean | Status |
|--------|-----|-------|--------|
| [source] | ✓ / ✗ | ✓ / ✗ | Complete / In progress / Pending |

5. Flag any missing folders or empty directories.
6. Note what step in the pipeline each source is currently at.
