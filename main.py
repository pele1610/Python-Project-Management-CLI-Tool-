import argparse
from models import User, Project, Task
from utils import load_data, save_data, print_success, print_error, print_info
from utils import display_users, display_projects, display_tasks
from utils.validators import validate_email, validate_date, validate_not_empty




def add_user(args):
    """Create a new user and save to users.json."""
    try:
        name = validate_not_empty(args.name, "Name")
        email = validate_not_empty(args.email, "Email")

        if not validate_email(email):
            print_error("Invalid email address.")
            return  
        
        data = load_data("users")

        for u in data.values():
            if u["email"] == email:
                print_error(f"A user with email '{email}' already exists.") 
                return



        user = User(name, email)
        data[str(user.user_id)] = user.to_dict()
        save_data("users", data)
        print_success(f"User '{name}' created with ID #{user.user_id}.")
    except ValueError as e:
        print_error(str(e))


def list_users(args):
    """Display all users in a table"""
    data = load_data("users")
    if not data:
        print_info("No users found.")
        return
    users = [User.from_dict(u) for u in data.values()]
    display_users(users)


    #project commands


def add_project(args):
    """Create a new project and save to projects.json."""
    try:
        title = validate_not_empty(args.title, "Title")
        owner = validate_not_empty(args.user, "User")

        if args.due_date and not validate_date(args.due_date):
            print_error("Invalid date format. Use YYYY-MM-DD.")
            return
        

        users_data = load_data("users")
        user_record = None
        user_key = None



        for key, u in users_data.items():
            if u["name"].lower() == owner.lower():
                user_record = u
                user_key = key
                break

        if not user_record:
            print_error(f"No user found with name '{owner}'.")
            return
        

        projects_data = load_data("projects")
        for p in projects_data.values():
            if p["title"].lower() == title.lower():
                print_error(f"Project '{title}' already exists.")
                return

        project = Project(
            title=title,
            owner=user_record["name"],
            description=args.description or "",
            due_date=args.due_date or ""
        )

        user = User.from_dict(user_record)
        user.add_project(title)
        users_data[user_key] = user.to_dict()

        projects_data[str(project._id)] = project.to_dict()
        save_data("projects", projects_data)
        save_data("users", users_data)
        print_success(f"Project '{title}' created and assigned to '{user.name}'.")

    except ValueError as e:
        print_error(str(e))


def list_projects(args):
    """List all projects or filter by user."""
    data = load_data("projects")
    if not data:
        print_info("No projects found.")
        return

    projects = [Project.from_dict(p) for p in data.values()]

    if args.user:
        projects = [p for p in projects if p.owner.lower() == args.user.lower()]
        if not projects:
            print_info(f"No projects found for user '{args.user}'.")
            return

    display_projects(projects)


# Task commands

def add_task(args):
    """Create a new task and assign it to a project."""
    try:
        title = validate_not_empty(args.title, "Title")
        project_title = validate_not_empty(args.project, "Project")

        projects_data = load_data("projects")
        project_record = None
        project_key = None

        for key, p in projects_data.items():
            if p["title"].lower() == project_title.lower():
                project_record = p
                project_key = key
                break

        if not project_record:
            print_error(f"Project '{project_title}' not found.")
            return

        tasks_data = load_data("tasks")
        for t in tasks_data.values():
            if t["title"].lower() == title.lower() and t["project_title"].lower() == project_title.lower():
                print_error(f"Task '{title}' already exists in project '{project_title}'.")
                return

        task = Task(
            title=title,
            project_title=project_record["title"],
            assigned_to=args.assigned_to or ""
        )

        project = Project.from_dict(project_record)
        project.add_task(title)
        projects_data[project_key] = project.to_dict()

        tasks_data[str(task._id)] = task.to_dict()
        save_data("tasks", tasks_data)
        save_data("projects", projects_data)
        print_success(f"Task '{title}' added to project '{project.title}'.")

    except ValueError as e:
        print_error(str(e))


def list_tasks(args):
    """List all tasks or filter by project."""
    data = load_data("tasks")
    if not data:
        print_info("No tasks found.")
        return

    tasks = [Task.from_dict(t) for t in data.values()]

    if args.project:
        tasks = [t for t in tasks if t.project_title.lower() == args.project.lower()]
        if not tasks:
            print_info(f"No tasks found for project '{args.project}'.")
            return

    display_tasks(tasks)


def complete_task(args):
    """Mark a task as done."""
    try:
        title = validate_not_empty(args.title, "Title")
        data = load_data("tasks")

        for key, t in data.items():
            if t["title"].lower() == title.lower():
                t["status"] = "done"
                save_data("tasks", data)
                print_success(f"Task '{title}' marked as done.")
                return

        print_error(f"Task '{title}' not found.")

    except ValueError as e:
        print_error(str(e))


#CLI setup

def main():
    parser = argparse.ArgumentParser(
        description="Project Tracker CLI",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    p_add_user = subparsers.add_parser("add-user", help="Add a new user")
    p_add_user.add_argument("--name", required=True, help="User's full name")
    p_add_user.add_argument("--email", required=True, help="User's email")
    p_add_user.set_defaults(func=add_user)

    # list-users
    p_list_users = subparsers.add_parser("list-users", help="List all users")
    p_list_users.set_defaults(func=list_users)

    # add-project
    p_add_project = subparsers.add_parser("add-project", help="Add a new project")
    p_add_project.add_argument("--title", required=True, help="Project title")
    p_add_project.add_argument("--user", required=True, help="Owner's name")
    p_add_project.add_argument("--description", help="Project description")
    p_add_project.add_argument("--due-date", dest="due_date", help="Due date YYYY-MM-DD")
    p_add_project.set_defaults(func=add_project)

    # list-projects
    p_list_projects = subparsers.add_parser("list-projects", help="List all projects")
    p_list_projects.add_argument("--user", help="Filter by user name")
    p_list_projects.set_defaults(func=list_projects)

    # add-task
    p_add_task = subparsers.add_parser("add-task", help="Add a task to a project")
    p_add_task.add_argument("--title", required=True, help="Task title")
    p_add_task.add_argument("--project", required=True, help="Project title")
    p_add_task.add_argument("--assigned-to", dest="assigned_to", help="Assign to a user")
    p_add_task.set_defaults(func=add_task)

    # list-tasks
    p_list_tasks = subparsers.add_parser("list-tasks", help="List all tasks")
    p_list_tasks.add_argument("--project", help="Filter by project title")
    p_list_tasks.set_defaults(func=list_tasks)

    # complete-task
    p_complete_task = subparsers.add_parser("complete-task", help="Mark a task as done")
    p_complete_task.add_argument("--title", required=True, help="Task title")
    p_complete_task.set_defaults(func=complete_task)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()
