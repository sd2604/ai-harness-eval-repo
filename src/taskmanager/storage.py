"""JSON file persistence for tasks."""
import json
import os


def load_all(path):
    """Load the full list of task dicts currently on disk."""
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_tasks(path, manager_tasks, category="default"):
    """Save this manager's tasks under `category`, without clobbering
    other categories that may already be stored in the same file.
    """
    existing = load_all(path)
    # existing is a list of {"category": ..., "tasks": [...]}
    by_category = {entry["category"]: entry["tasks"] for entry in existing}
    by_category[category] = [t.to_dict() for t in manager_tasks]

    merged = [{"category": cat, "tasks": tasks} for cat, tasks in by_category.items()]
    with open(path, "w") as f:
        json.dump(merged, f, indent=2)


def load_category(path, category="default"):
    """Load just one category's task dicts."""
    existing = load_all(path)
    for entry in existing:
        if entry["category"] == category:
            return entry["tasks"]
    return []
