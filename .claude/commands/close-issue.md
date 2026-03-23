Close a GitHub issue with a summary comment.

The user will provide the issue number as an argument (e.g. `/close-issue 3`).

Steps:
1. Run `gh issue view [N]` to read the issue title and body.
2. Ask the user: "What was done to resolve this issue?" (wait for their response).
3. Post a closing comment with `gh issue comment [N] --body "[summary]"`.
4. Close the issue with `gh issue close [N]`.
5. Confirm: "Issue #[N] closed."

If no number is provided, ask the user which issue to close.
