# Harness Evaluation Repo

This repo exists to test the AI harness on real (seeded) bugs — not to be a
real product. It has three branches, each a "starting state" for one issue.

## Structure
- `master` — the clean, correct reference solution (all 10 tests pass)
- `issue-1-easy` — one-line logic bug in `priority.py` (sort order reversed)
- `issue-2-medium` — two related bugs in `tasks.py` (completion doesn't
  timestamp, and doesn't get filtered out of active tasks)
- `issue-3-hard` — a data-loss bug in `storage.py` (saving one category
  wipes out others already on disk)
- `issues/ISSUE_0X_*.md` — the GitHub-issue-style text to feed your harness
  for each branch (symptom + repro steps, not the fix)

## Running an evaluation
```bash
pip install -r requirements.txt
./scripts/run_issue.sh 1     # or 2, or 3
```
This checks out the buggy branch, shows you the issue text and the failing
tests, then tells you to point your harness at this checkout with that issue
text. When your harness is done, run:
```bash
python3 -m pytest tests/ -q
```
10/10 passing = issue resolved. Fewer = check which test(s) still fail to see
what the harness missed.

## Pushing this to GitHub (do this once, from scratch)

1. Create an empty repo on GitHub (no README/license — this repo already
   has everything): via the web UI, or with the CLI:
   ```bash
   gh repo create your-username/harness-eval-repo --private --source=. --remote=origin
   ```
2. If you didn't use `gh repo create` with `--source`, add the remote
   manually and push everything, branches and tags included:
   ```bash
   git remote add origin https://github.com/your-username/harness-eval-repo.git
   git push -u origin master
   git push origin issue-1-easy issue-2-medium issue-3-hard
   git push origin reference-solution
   ```
3. Optionally, open each `issues/ISSUE_0X_*.md` as an actual GitHub Issue
   (Issues tab → New Issue → paste the content) so your harness can be
   pointed at a real issue URL/number instead of a local file, if your
   harness's issue-ingestion step expects that.

## Adding more issues later
Follow the same pattern: branch from `master`, make one deliberate
regression, confirm the relevant test(s) fail, commit, write the issue
markdown describing only the symptom. Keep the reference solution on
`master` untouched so it's always your ground truth.
