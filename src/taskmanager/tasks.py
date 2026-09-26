"""Core Task and TaskManager classes."""
from datetime import datetime, timezone


class Task:
    def __init__(self, title, priority=3):
        self.title = title
        self.priority = priority
        self.completed = False
        self.completed_at = None

    def complete(self):
        self.completed = True
        self.completed_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority=3):
        task = Task(title, priority)
        self.tasks.append(task)
        return task

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.complete()
                return task
        return None

    def active_tasks(self):
        """Tasks that are not yet completed."""
        return [t for t in self.tasks if not t.completed]

    def completed_tasks(self):
        return [t for t in self.tasks if t.completed]
