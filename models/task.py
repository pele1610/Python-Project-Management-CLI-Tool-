from datetime import datetime

VALID_STATUSES = {"todo", "in_progress", "done"}


class Task:

    _id_counter = 0

    def __init__(self, title: str, project_title: str, status: str = "todo",
                 assigned_to: str = "", task_id: int = None, created_at: str = None):
        