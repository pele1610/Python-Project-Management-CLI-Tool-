# Project Tracker

A simple command-line project tracker for managing users, projects, and tasks using JSON storage.

## Overview

This repository contains a lightweight CLI application for:
- Adding and listing users
- Creating and tracking projects
- Adding task items to projects
- Marking tasks as complete

Data is stored in the `data/` folder as JSON files:
- `data/users.json`
- `data/projects.json`
- `data/tasks.json`

## Requirements

- Python 3.8+
- `rich`
- `tabulate`

Install required packages with:

```bash
pip install -r requirements.txt
```

## Running the CLI

Run the application from the repository root:

```bash
python main.py <command> [options]
```

### Commands

- `add-user --name NAME --email EMAIL`
  - Add a new user.
- `list-users`
  - List all users.
- `add-project --title TITLE --user OWNER [--description DESC] [--due-date YYYY-MM-DD]`
  - Create a new project and assign it to a user.
- `list-projects [--user OWNER]`
  - List all projects, optionally filtering by owner.
- `add-task --title TITLE --project PROJECT [--assigned-to NAME]`
  - Create a task for an existing project.
- `list-tasks [--project PROJECT]`
  - List all tasks, optionally filtering by project.
- `complete-task --title TITLE`
  - Mark a task as done.

## Examples

Add a user:

```bash
python main.py add-user --name "Alice Smith" --email alice@example.com
```

Create a project for a user:

```bash
python main.py add-project --title "Website Redesign" --user "Alice Smith" --description "Refresh the homepage" --due-date 2026-07-01
```

Add a task to a project:

```bash
python main.py add-task --title "Design mockups" --project "Website Redesign" --assigned-to "Alice Smith"
```

List tasks for a project:

```bash
python main.py list-tasks --project "Website Redesign"
```

## Project Structure

- `main.py` - CLI command definitions and entry point.
- `models/` - Data models for users, projects, tasks.
- `utils/` - Data loading/saving, validation, and display helpers.
- `tests/` - Unit tests for CLI behavior.
- `data/` - JSON storage for application data.

## Testing

Run the unit tests with:

```bash
python -m unittest
```

## Notes

- `users` are looked up by name when assigning projects.
- Projects and tasks are stored in JSON and persist between runs.
- Email and date inputs are validated before data is saved.
