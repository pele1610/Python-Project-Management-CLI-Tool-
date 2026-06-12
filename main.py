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
        

        
