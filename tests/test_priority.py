import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from taskmanager.tasks import TaskManager
from taskmanager.priority import sort_by_priority, top_priority_task


def test_sort_by_priority_highest_first():
    mgr = TaskManager()
    mgr.add_task("low", priority=1)
    mgr.add_task("high", priority=5)
    mgr.add_task("mid", priority=3)
    ordered = sort_by_priority(mgr.tasks)
    assert [t.title for t in ordered] == ["high", "mid", "low"]


def test_top_priority_task_returns_most_urgent():
    mgr = TaskManager()
    mgr.add_task("low", priority=1)
    mgr.add_task("high", priority=5)
    top = top_priority_task(mgr.tasks)
    assert top.title == "high"


def test_top_priority_ignores_completed():
    mgr = TaskManager()
    mgr.add_task("low", priority=1)
    urgent = mgr.add_task("high", priority=5)
    mgr.complete_task(urgent.title)
    top = top_priority_task(mgr.tasks)
    assert top.title == "low"


def test_top_priority_empty_returns_none():
    mgr = TaskManager()
    assert top_priority_task(mgr.tasks) is None
