from rich.console import Console
from rich.table import Table    
from rich import box

console = Console()


def print_success(message: str):
    console.print(f"[bold green]OK:{message}[/bold green]")



def print_error(message: str):
    console.print(f"[bold red]ERROR:{message}[/bold red]")



def print_info(message: str):
    console.print(f"[bold blue]INFO:{message}[/bold blue]")


def display_users(users: list):
    table = Table(title="Users", box=box.ROUNDED)
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="White")
    table.add_column("Email", style="White")
    table.add_column("Projects", style="green")



    for user in users:
        table.add_row(
            str(user.id),
            user.name,
            user.email,
            str(len(user.project_titles))

        )
    console.print(table)



def display_projects(projects: list):
    table = Table(title="Projects", box=box.ROUNDED)
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="White")
    table.add_column("owner", style="White")
    table.add_column("Due Date", style="white")
    table.add_column("Tasks", style="green")

    for project in projects:
        table.add_row(
            str(project._id),
            project.title,
            project.owner,
            project.due_date,
            str(len(project.task_titles))
        )
    console.print(table)


def display_tasks(tasks: list):
    table = Table(title="Tasks", box=box.ROUNDED)
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="White")
    table.add_column("Status", style="yellow")
    table.add_column("Assigned To", style="green")
    table.add_column("Created",style="white")


    for task in tasks:
        status_color = {"todo": "red", "in_progress": "yellow", "done": "green"}
        color = status_color.get(task.status, "white")
        table.add_row(
            str(task._id),
            task.title,
            f"[{color}]{task.status}[/{color}]",
            task.assigned_to or "Unassigned",
            task.created_at 
        )
    console.print(table)


    