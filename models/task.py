from datetime import datetime

VALID_STATUSES = {"todo", "in_progress", "done"}


class Task:

    _id_counter = 0

    def __init__(self, title: str, project_title: str, status: str = "todo",
                 assigned_to: str = "", task_id: int = None, created_at: str = None):
        

        if task_id is not None:
            self.id = task_id
            Task._id_counter = max(Task._id_counter, task_id)
        else:
            Task._id_counter += 1
            self.id = Task._id_counter

        self.title = title
        self.project_title = project_title
        self.assigned_to = assigned_to
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if status not in VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Choose: {VALID_STATUSES}")
        self.status = status


    def compelete(self):
        self.status = "done"


    def __str__(self):
        icons = {"todo": "[ ]", "in_progress": "[~]", "done": "[x]"}
        icons = icons[self.status]
        assignee =self.assigned_to or "Unassigned"
        return f"{icons} [#{self.id}] {self.title} ({self.status}) → {assignee}"
    

    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "project_title": self.project_title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at
        }


    @classmethod
    def from_dict(cls, date:dict):
        return cls(
            title=date["title"],
            project_title=date["project_title"],
            status=date.get("status", "todo"),
            assigned_to=date.get("assigned_to", ""),
            task_id=date.get("id"),
            created_at=date.get("created_at")
        )