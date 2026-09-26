# [Bug] Completed tasks still show up as active, and have no completion time

**Branch to evaluate on:** `issue-2-medium`

## Description
Two things seem broken with task completion:

1. After marking a task complete, it still appears in the list returned by
   `active_tasks()` — as if it was never completed.
2. There doesn't seem to be any record of *when* a task was completed.

I'm not sure if these are the same root cause or two separate bugs — please
investigate both.

## Steps to reproduce
```python
mgr = TaskManager()
mgr.add_task("A")
mgr.add_task("B")
mgr.complete_task("A")
print(len(mgr.active_tasks()))       # I expect 1, not 2
print(mgr.tasks[0].completed_at)     # I expect a timestamp, not None
```

## Expected behavior
- `active_tasks()` should only return tasks that are not yet completed.
- A completed task should have `completed_at` set to the time it was
  completed.

## Actual behavior
- `active_tasks()` returns all tasks regardless of completion status.
- `completed_at` stays `None` even after calling `complete_task`.

## Acceptance criteria
All tests in `tests/test_tasks.py` pass.
