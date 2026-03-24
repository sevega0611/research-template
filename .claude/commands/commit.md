Stage all changes, commit, and push to GitHub.

The user may optionally provide a commit message as an argument (e.g. `/commit "add scraping script"`).

Steps:
1. Run `git status` to show the user what will be committed.
2. Run `git branch --show-current` to check the current branch.
3. If the current branch is `main`, warn the user:
   "⚠️ Estás en main. Se recomienda trabajar en un branch por issue. ¿Quieres continuar de todas formas o crear un branch primero con /start?"
   Wait for confirmation before proceeding.
4. If no message was provided, ask: "¿Cuál es el mensaje del commit? (formato recomendado: #n descripción)"
5. Run:
   ```
   git add .
   git commit -m "[message]"
   git push
   ```
6. Confirm: "Pushed to GitHub. Commit: [message]"

Note: Never commit `.env` files or data files. Check `.gitignore` is in place before staging.
