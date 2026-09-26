# AI Harness Evaluation Repo

This repository is an evaluation environment for testing an AI coding agent.

The codebase contains intentionally seeded bugs. The AI agent is given an issue describing the expected behavior and must modify the code until the test suite passes.

## Current Task

### Issue 01 — Priority Ordering

**Difficulty:** Easy

Tasks are currently sorted in the wrong priority order.

Higher priority values should be treated as more urgent.

For example:

- priority 5 → high
- priority 3 → medium
- priority 1 → low

## Expected Behavior

The highest-priority task should be returned first.

The following tests should pass after the bug is fixed:

- `test_sort_by_priority_highest_first`
- `test_top_priority_task_returns_most_urgent`

## Evaluation

Run the test suite with:

```bash
python3 -m pytest