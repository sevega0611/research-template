Show a summary of activity this week.

Steps:
1. Run `git log --since="7 days ago" --oneline --all` to get recent commits.
2. Run `gh issue list --state all --search "updated:>$(date -v-7d +%Y-%m-%d)"` to get recently updated issues.
3. Summarize:
   - Commits made this week (author, message)
   - Issues opened this week
   - Issues closed this week
   - Overall progress assessment based on CLAUDE.md pipeline status
4. Keep the summary concise and readable.
