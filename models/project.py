from datetime import datetime


class Project:
    """Represents a project owned by a user."""

    _id_counter = 0

    def __init__(self, title: str, owner: str, description: str = "",
                 due_date: str = "", project_id: int = None, created_at: str = None):

        if project_id is not None:
            self._id = project_id
            Project._id_counter = max(Project._id_counter, project_id)
        else:
            Project._id_counter += 1
            self._id = Project._id_counter

        self.title = title
        self.owner = owner
        self.description = description
        self.due_date = due_date
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")
        self.task_titles = []

    def add_task(self, title: str):
        if title in self.task_titles:
            raise ValueError(f"Task '{title}' already exists in project '{self.title}'.")
        self.task_titles.append(title)

    def __str__(self):
        return f"[#{self._id}] {self.title} (owner: {self.owner}) — {len(self.task_titles)} task(s)"

    def to_dict(self):
        return {
            "id": self._id,
            "title": self.title,
            "owner": self.owner,
            "description": self.description,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "task_titles": self.task_titles
        }

    @classmethod
    def from_dict(cls, data: dict):
        p = cls(
            title=data["title"],
            owner=data["owner"],
            description=data.get("description", ""),
            due_date=data.get("due_date", ""),
            project_id=data["id"],
            created_at=data.get("created_at")
        )
        p.task_titles = data.get("task_titles", [])
        return p