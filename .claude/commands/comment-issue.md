Add a comment to a GitHub issue.

The user will provide the issue number as an argument (e.g. `/comment-issue 2`).

Steps:
1. Run `gh issue view [N]` to show the user the current issue context.
2. Ask: "What would you like to say in this comment?"
3. Post the comment with `gh issue comment [N] --body "[user's message]"`.
4. Confirm: "Comment added to issue #[N]."

If no number is provided, ask the user which issue to comment on.
