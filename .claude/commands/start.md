Start working on a GitHub issue by creating a new branch.

Steps:
1. Run `git branch` to show the current branch and existing branches.
2. Run `git checkout main && git pull` to make sure main is up to date.
3. Ask the user: "¿En qué issue vas a trabajar? (número y nombre)"
4. Create the branch with the format `issue{n}_{name}` where name is lowercase with hyphens:
   ```
   git checkout -b issue{n}_{name}
   ```
5. Confirm: "Branch creado: issue{n}_{name}. Ya puedes empezar a trabajar."

Example: if the user says "issue 5, LexisNexis scraping", create branch `issue5_lexisnexis-scraping`.

Note: Always start from an updated main branch. Never create a branch from another branch.
