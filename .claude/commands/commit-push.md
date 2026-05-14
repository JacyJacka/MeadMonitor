Follow these steps in order, waiting for user input at each stage before proceeding:

## Step 1 — Branch

Run `git branch` to list existing branches and identify the current one.

Ask the user: "Which branch should changes be committed to?" Show the current branch as the default option. If the user names a branch that does not exist in the output of `git branch`, create it with `git checkout -b <branch>`. If it already exists, check it out with `git checkout <branch>` (unless it is already the current branch, in which case skip).

## Step 2 — Commit

Run `git status` and `git diff` to show the user what will be committed.

Ask the user for a commit message. Once provided, stage all modified and untracked files with `git add` (prefer specific file names over `git add .` to avoid accidentally including secrets or binaries — list the files from `git status` and add them individually), then commit using the message supplied by the user. Use a HEREDOC to pass the message to `git commit -m` to preserve formatting.

Do NOT add a "Co-Authored-By" trailer unless the user explicitly asks for it.

## Step 3 — Push

Ask the user: "Should this branch be pushed to the remote?" If the user says yes, run `git push` (with `-u origin <branch>` if the branch has no upstream yet). If no, stop here.

Report the final status after each git command.
