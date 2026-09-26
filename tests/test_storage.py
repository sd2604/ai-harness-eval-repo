import sys, os, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from taskmanager.tasks import TaskManager
from taskmanager.storage import save_tasks, load_category


def test_save_and_load_roundtrip():
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "tasks.json")
        mgr = TaskManager()
        mgr.add_task("A")
        save_tasks(path, mgr.tasks, category="work")
        loaded = load_category(path, category="work")
        assert len(loaded) == 1
        assert loaded[0]["title"] == "A"


def test_save_does_not_clobber_other_categories():
    """Regression guard: saving 'personal' tasks must not wipe out
    'work' tasks already saved in the same file."""
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "tasks.json")

        work_mgr = TaskManager()
        work_mgr.add_task("Finish PRD")
        save_tasks(path, work_mgr.tasks, category="work")

        personal_mgr = TaskManager()
        personal_mgr.add_task("Buy groceries")
        save_tasks(path, personal_mgr.tasks, category="personal")

        work_after = load_category(path, category="work")
        personal_after = load_category(path, category="personal")

        assert len(work_after) == 1, "work tasks were wiped out by a later save"
        assert work_after[0]["title"] == "Finish PRD"
        assert len(personal_after) == 1
        assert personal_after[0]["title"] == "Buy groceries"
