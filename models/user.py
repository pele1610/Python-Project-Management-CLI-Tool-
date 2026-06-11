from models.person import Person

class User(Person):

    _id_counter = 0

    def __init__(self, name: str, email: str, user_id: int = None, project_titles: list = None):
        super().__init__(name, email)

        if user_id is not None:
            self.id = user_id
            User._id_counter = max(User._id_counter, user_id)
        else:
            User._id_counter += 1
            self.id = User._id_counter

        self.project_titles = project_titles if project_titles else []

    @property
    def user_id(self):
        return self.id

    def add_project(self, title: str):
        if title in self.project_titles:
            raise ValueError(f"Project '{title}' already assigned to {self.name}.")
        self.project_titles.append(title)

    def __str__(self):
        return f"[#{self.id}] {self.name} <{self.email}> -{len(self.project_titles)} project(s)"

    def to_dict(self):
        base = super().to_dict()
        base["id"] = self.id
        base["project_titles"] = self.project_titles
        return base

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            email=data["email"],
            user_id=data.get("id"),
            project_titles=data.get("project_titles", []),
        )