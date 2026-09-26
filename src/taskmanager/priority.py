"""Priority sorting/ranking logic."""


def sort_by_priority(tasks):
    """Return tasks sorted highest-priority first.

    Priority is an integer 1-5, where 5 is the most urgent.
    """
    return sorted(tasks, key=lambda t: t.priority)


def top_priority_task(tasks):
    """Return the single most urgent active task, or None if empty."""
    active = [t for t in tasks if not t.completed]
    if not active:
        return None
    return sort_by_priority(active)[0]
