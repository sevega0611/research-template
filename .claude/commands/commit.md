Stage all changes, commit, and push to GitHub.

The user may optionally provide a commit message as an argument (e.g. `/commit "add scraping script"`).

Steps:
1. Run `git status` to show the user what will be committed.
2. If no message was provided, ask: "What is the commit message?"
3. Run:
   ```
   git add .
   git commit -m "[message]"
   git push
   ```
4. Confirm: "Pushed to GitHub. Commit: [message]"

Note: Never commit `.env` files or data files. Check `.gitignore` is in place before staging.
