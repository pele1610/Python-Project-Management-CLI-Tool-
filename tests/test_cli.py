import unittest
from unittest.mock import patch, MagicMock
import main


class TestCLICommands(unittest.TestCase):
    """Tests for CLI command functions."""

    @patch("main.load_data")
    @patch("main.save_data")
    def test_add_user(self, mock_save, mock_load):
        """Test that add_user saves a new user."""
        mock_load.return_value = {}
        args = MagicMock()
        args.name = "TestUser"
        args.email = "test@test.com"
        main.add_user(args)
        mock_save.assert_called_once()

    @patch("main.load_data")
    @patch("main.save_data")
    def test_add_user_duplicate_email(self, mock_save, mock_load):
        """Test that duplicate email is rejected."""
        mock_load.return_value = {
            "1": {"name": "Alex", "email": "test@test.com", "id": 1, "project_titles": []}
        }
        args = MagicMock()
        args.name = "Another"
        args.email = "test@test.com"
        main.add_user(args)
        mock_save.assert_not_called()

    @patch("main.load_data")
    def test_list_users_empty(self, mock_load):
        """Test list_users when no users exist."""
        mock_load.return_value = {}
        args = MagicMock()
        main.list_users(args)

    @patch("main.load_data")
    @patch("main.save_data")
    def test_add_project_user_not_found(self, mock_save, mock_load):
        """Test that add_project fails if user does not exist."""
        mock_load.return_value = {}
        args = MagicMock()
        args.title = "My Project"
        args.user = "Ghost"
        args.description = ""
        args.due_date = ""
        main.add_project(args)
        mock_save.assert_not_called()

    @patch("main.load_data")
    def test_list_tasks_empty(self, mock_load):
        """Test list_tasks when no tasks exist."""
        mock_load.return_value = {}
        args = MagicMock()
        args.project = None
        main.list_tasks(args)

    @patch("main.load_data")
    @patch("main.save_data")
    def test_complete_task_not_found(self, mock_save, mock_load):
        """Test that complete_task fails if task does not exist."""
        mock_load.return_value = {}
        args = MagicMock()
        args.title = "Ghost Task"
        main.complete_task(args)
        mock_save.assert_not_called()


if __name__ == "__main__":
    unittest.main()