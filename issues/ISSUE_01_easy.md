# [Bug] Tasks are showing up in the wrong priority order

**Branch to evaluate on:** `issue-1-easy`

## Description
When I call `sort_by_priority()` or `top_priority_task()`, the results seem to
be backwards. I have tasks with priority 5 (very urgent) and priority 1 (not
urgent), and the "top priority" function is returning the priority-1 task
instead of the priority-5 one.

## Steps to reproduce
```python
mgr = TaskManager()
mgr.add_task("low", priority=1)
mgr.add_task("high", priority=5)
print(top_priority_task(mgr.tasks).title)
```

## Expected behavior
Should print `"high"` — priority 5 is the most urgent and should be returned
first.

## Actual behavior
Prints `"low"` instead.

## Acceptance criteria
All tests in `tests/test_priority.py` pass.
