import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from taskmanager.tasks import TaskManager


def test_complete_task_marks_completed():
    mgr = TaskManager()
    mgr.add_task("Write report")
    mgr.complete_task("Write report")
    assert mgr.tasks[0].completed is True


def test_complete_task_sets_timestamp():
    mgr = TaskManager()
    mgr.add_task("Write report")
    mgr.complete_task("Write report")
    assert mgr.tasks[0].completed_at is not None


def test_active_tasks_excludes_completed():
    mgr = TaskManager()
    mgr.add_task("A")
    mgr.add_task("B")
    mgr.complete_task("A")
    active = mgr.active_tasks()
    assert len(active) == 1
    assert active[0].title == "B"


def test_completed_tasks_only_returns_completed():
    mgr = TaskManager()
    mgr.add_task("A")
    mgr.add_task("B")
    mgr.complete_task("A")
    done = mgr.completed_tasks()
    assert len(done) == 1
    assert done[0].title == "A"
