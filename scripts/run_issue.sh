#!/usr/bin/env bash
# Usage: ./scripts/run_issue.sh <1|2|3>
#
# Checks out the buggy branch for the given issue number, prints the issue
# text your harness should receive, then (after you've run your harness
# against this checkout) scores the result by running the relevant tests.
set -e

ISSUE_NUM="$1"
if [ -z "$ISSUE_NUM" ]; then
  echo "Usage: $0 <1|2|3>"
  exit 1
fi

case "$ISSUE_NUM" in
  1) BRANCH="issue-1-easy";   ISSUE_FILE="issues/ISSUE_01_easy.md";   TEST_TARGET="tests/test_priority.py" ;;
  2) BRANCH="issue-2-medium"; ISSUE_FILE="issues/ISSUE_02_medium.md"; TEST_TARGET="tests/test_tasks.py" ;;
  3) BRANCH="issue-3-hard";   ISSUE_FILE="issues/ISSUE_03_hard.md";   TEST_TARGET="tests/test_storage.py" ;;
  *) echo "Unknown issue number: $ISSUE_NUM"; exit 1 ;;
esac

echo "=== Checking out $BRANCH (issue $ISSUE_NUM starting state) ==="
git checkout -q "$BRANCH"

echo ""
echo "=== Issue text to feed your harness ==="
cat "$ISSUE_FILE"

echo ""
echo "=== Baseline (should show failing tests before your harness runs) ==="
python3 -m pytest "$TEST_TARGET" -q || true

echo ""
echo ">>> Now run your harness against this checkout, pointed at $ISSUE_FILE."
echo ">>> When it's done, re-run: python3 -m pytest tests/ -q"
echo ">>> All tests passing (10/10) = issue resolved."
