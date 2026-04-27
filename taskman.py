#!/usr/bin/env python3
"""
TaskMan - A CLI Task Manager
Author: You!
Description: A command-line tool to manage tasks with priorities, due dates, and persistence.
"""

import json
import os
import sys
from datetime import datetime

# File where tasks are saved
TASKS_FILE = "tasks.json"

# Priority levels
PRIORITIES = {"high": "🔴", "medium": "🟡", "low": "🟢"}


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, priority="medium", due_date=None):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority.lower(),
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "due_date": due_date or "No due date",
    }
    tasks.append(task)
    save_tasks(tasks)
    icon = PRIORITIES.get(priority.lower(), "🟡")
    print(f"\n✅ Task added! {icon} [{priority.upper()}] '{title}'")


def list_tasks(show_done=False):
    """List all tasks."""
    tasks = load_tasks()

    if not tasks:
        print("\n📭 No tasks yet! Add one with: python taskman.py add 'Your task'")
        return

    print("\n" + "=" * 55)
    print("           📋  YOUR TASKS")
    print("=" * 55)

    active = [t for t in tasks if not t["done"]]
    done = [t for t in tasks if t["done"]]

    if active:
        print("\n  PENDING:")
        for task in active:
            icon = PRIORITIES.get(task["priority"], "🟡")
            print(f"\n  [{task['id']}] {icon} {task['title']}")
            print(f"       Priority : {task['priority'].capitalize()}")
            print(f"       Due      : {task['due_date']}")
            print(f"       Added    : {task['created']}")

    if show_done and done:
        print("\n  COMPLETED:")
        for task in done:
            print(f"\n  [✓] ~~{task['title']}~~")

    if not show_done and done:
        print(f"\n  ({len(done)} completed task(s) hidden — use 'list --all' to show)")

    print("\n" + "=" * 55)
    print(f"  Total: {len(active)} pending | {len(done)} done")
    print("=" * 55 + "\n")


def complete_task(task_id):
    """Mark a task as complete."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"\n🎉 Nice work! Task #{task_id} '{task['title']}' marked as done.")
            return
    print(f"\n❌ Task #{task_id} not found.")


def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    original_count = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) < original_count:
        save_tasks(tasks)
        print(f"\n🗑️  Task #{task_id} deleted.")
    else:
        print(f"\n❌ Task #{task_id} not found.")


def show_help():
    """Show usage instructions."""
    print("""
╔══════════════════════════════════════════════╗
║          TaskMan - CLI Task Manager          ║
╚══════════════════════════════════════════════╝

USAGE:
  python taskman.py <command> [options]

COMMANDS:
  add <title> [priority] [due_date]
      Add a new task
      Priority: high | medium | low  (default: medium)
      Example: python taskman.py add "Buy groceries" high "2024-12-01"

  list
      Show all pending tasks

  list --all
      Show all tasks including completed ones

  done <id>
      Mark a task as complete
      Example: python taskman.py done 1

  delete <id>
      Delete a task
      Example: python taskman.py delete 2

  help
      Show this help message
""")


def main():
    args = sys.argv[1:]

    if not args or args[0] == "help":
        show_help()

    elif args[0] == "add":
        if len(args) < 2:
            print("❌ Usage: python taskman.py add 'Task title' [priority] [due_date]")
        else:
            title = args[1]
            priority = args[2] if len(args) > 2 else "medium"
            due_date = args[3] if len(args) > 3 else None
            if priority not in PRIORITIES:
                print(f"❌ Invalid priority '{priority}'. Use: high, medium, or low")
            else:
                add_task(title, priority, due_date)

    elif args[0] == "list":
        show_done = "--all" in args
        list_tasks(show_done)

    elif args[0] == "done":
        if len(args) < 2:
            print("❌ Usage: python taskman.py done <task_id>")
        else:
            complete_task(int(args[1]))

    elif args[0] == "delete":
        if len(args) < 2:
            print("❌ Usage: python taskman.py delete <task_id>")
        else:
            delete_task(int(args[1]))

    else:
        print(f"❌ Unknown command '{args[0]}'. Run 'python taskman.py help' for usage.")


if __name__ == "__main__":
    main()
