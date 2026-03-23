Generate a daily progress report and save it to the reports/ folder.

Steps:
1. Ask the user: "Anything to add to today's report? (calls, decisions, blockers, ideas)" — wait for their response.
2. Gather report content:
   - Run `git log --since="midnight" --oneline` to get today's commits
   - Run `git diff --name-only HEAD~1 HEAD` for files changed in the last commit
   - Run `gh issue list --state all --search "updated:>$(date +%Y-%m-%d)"` for today's issue activity
   - Check for new or modified files in Dropbox raw/ and clean/ folders
3. Write the report as `reports/report_YYYY-MM-DD.md` with sections:
   - **Commits** — with message and files changed
   - **Scripts** — new or modified scripts with brief description
   - **Data** — new or modified files in raw/ and clean/
   - **Issues** — opened, closed, or commented today
   - **Notes** — manual notes provided by the user
4. Commit the report: `git add reports/ && git commit -m "add daily report YYYY-MM-DD" && git push`
5. Confirm: "Report saved and committed."
