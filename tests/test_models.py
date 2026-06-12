import unittest
from models.user import User
from models.project import Project
from models.task import Task


class TestUser(unittest.TestCase):
    """Tests for the User class."""

    def test_create_user(self):
        """Test that a user is created with correct attributes."""
        user = User("Alex", "alex@test.com")
        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.email, "alex@test.com")

    def test_user_id_increments(self):
        """Test that each new user gets a unique ID."""
        user1 = User("Alex", "alex@test.com")
        user2 = User("Bob", "bob@test.com")
        self.assertNotEqual(user1.user_id, user2.user_id)

    def test_add_project(self):
        """Test that a project title can be added to a user."""
        user = User("Alex", "alex@test.com")
        user.add_project("CLI Tool")
        self.assertIn("CLI Tool", user.project_titles)

    def test_add_duplicate_project(self):
        """Test that adding a duplicate project raises an error."""
        user = User("Alex", "alex@test.com")
        user.add_project("CLI Tool")
        with self.assertRaises(ValueError):
            user.add_project("CLI Tool")

    def test_to_dict(self):
        """Test that to_dict returns correct keys."""
        user = User("Alex", "alex@test.com")
        d = user.to_dict()
        self.assertIn("name", d)
        self.assertIn("email", d)
        self.assertIn("id", d)

    def test_from_dict(self):
        """Test that from_dict reconstructs a User correctly."""
        data = {"name": "Alex", "email": "alex@test.com", "id": 99, "project_titles": []}
        user = User.from_dict(data)
        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.user_id, 99)


class TestProject(unittest.TestCase):
    """Tests for the Project class."""

    def test_create_project(self):
        """Test that a project is created with correct attributes."""
        project = Project("CLI Tool", "Alex")
        self.assertEqual(project.title, "CLI Tool")
        self.assertEqual(project.owner, "Alex")

    def test_add_task(self):
        """Test that a task title can be added to a project."""
        project = Project("CLI Tool", "Alex")
        project.add_task("Write tests")
        self.assertIn("Write tests", project.task_titles)

    def test_add_duplicate_task(self):
        """Test that adding a duplicate task raises an error."""
        project = Project("CLI Tool", "Alex")
        project.add_task("Write tests")
        with self.assertRaises(ValueError):
            project.add_task("Write tests")

    def test_to_dict(self):
        """Test that to_dict returns correct keys."""
        project = Project("CLI Tool", "Alex")
        d = project.to_dict()
        self.assertIn("title", d)
        self.assertIn("owner", d)
        self.assertIn("id", d)


class TestTask(unittest.TestCase):
    """Tests for the Task class."""

    def test_create_task(self):
        """Test that a task is created with correct attributes."""
        task = Task("Write tests", "CLI Tool")
        self.assertEqual(task.title, "Write tests")
        self.assertEqual(task.status, "todo")

    def test_complete_task(self):
        """Test that complete() changes status to done."""
        task = Task("Write tests", "CLI Tool")
        task.complete()
        self.assertEqual(task.status, "done")

    def test_invalid_status(self):
        """Test that an invalid status raises an error."""
        with self.assertRaises(ValueError):
            Task("Write tests", "CLI Tool", status="invalid")

    def test_to_dict(self):
        """Test that to_dict returns correct keys."""
        task = Task("Write tests", "CLI Tool")
        d = task.to_dict()
        self.assertIn("title", d)
        self.assertIn("status", d)
        self.assertIn("id", d)

    def test_from_dict(self):
        """Test that from_dict reconstructs a Task correctly."""
        data = {
            "id": 1,
            "title": "Write tests",
            "project_title": "CLI Tool",
            "status": "todo",
            "assigned_to": "",
            "created_at": "2025-01-01 00:00"
        }
        task = Task.from_dict(data)
        self.assertEqual(task.title, "Write tests")
        self.assertEqual(task.status, "todo")


if __name__ == "__main__":
    unittest.main()