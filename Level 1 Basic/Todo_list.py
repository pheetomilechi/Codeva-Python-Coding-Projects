import os

todo_List = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("\n" + "="*30)
    print("     CLI TO-DO LIST APP")
    print("="*30)
    print("1. View To-do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Clear All Tasks")
    print("5. Exit Application")
    print("="*30)


def view_tasks():
    clear_screen()
    print("-- CURRENT TO-DO LIST --")
    if not todo_List:
        print("[Your list is currently empty. Add a task to get started!]")
    else:
        for index, task in enumerate(todo_List, start=1):
            print(f"{index}. {task}")


def add_task():
    clear_screen()
    task = input("Enter the task description: ").strip()
    if task:
        todo_List.append(task)
        print(f"\nSuccess: '{task}' has been added!")
    else:
        print("\nError: Task description cannot be empty.")


def delete_task():
    view_tasks()
    if not todo_List:
        return

    print("\n" + "_"*20)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(todo_List):
            removed_task = todo_List.pop(task_num - 1)
            print(f"\nSuccess: '{removed_task}' has been removed!")
        else:
            print(
                "\nError: Invalid task number. Please select a valid number from the list.")
    except ValueError:
        print("\nError: Please enter a valid integer choice.")


def clear_all_tasks():
    clear_screen()
    confirm = input(
        "Are you sure you want to delete ALL tasks? (yes/no): ").lower().strip()
    if confirm == 'yes':
        todo_List.clear()
        print("\nSuccess: All tasks have been cleared.")
    else:
        print("\nAction canceled.")


def main():
    clear_screen()
    while True:
        show_menu()
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            clear_all_tasks()
        elif choice == '5':
            print("\nThank you for using the To-Do List App. Goodbye!")
            break
        else:
            clear_screen()
            print("\nInvalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()


# import argparse
# from random import choices

# FILENAME ="todo.txt"

# def add_strikethrough(item):
#     return f"\x1b[9m{item}\x1b[0m"

# def add(item):
#     with open(FILENAME, "a") as file:
#         file.write(f"{item}\n")
#         file.close()
#         print(f"Added item: {item}")

# def list_items():
#     lines = None
#     try:
#         with open(FILENAME, "r") as file:
#             lines = file.readlines()
#     except FileNotFoundError:
#         print(f"Error: File '{FILENAME}' not found")
#     if not lines:
#         print("No items found")
#     else:
#         print(lines)
#         for i, line in enumerate(lines):
#             print(f"{i+1}, {line.strip()}")

#     def mark_item_done(item_number):
#         with open(FILENAME, "r") as file:
#             lines = file.readlines()

#         if not lines:
#             print("Invalid item number.")
#         elif item_number < 1 or item_number > len(lines):
#             print("Invalid item number")

#             item = lines[item_number-1].rstrip()
#             item = add_strikethrough(item)
#             with open(FILENAME, "w") as file:
#                 for i, line in enumerate(lines):
#                     if i == item_number-1:
#                         file.write(f"{item}\n")
#                         print(f"Marked item as done: {item}")
#                     else:
#                         print(line)
#                         file.write(line)

#     if __name__ == "__main__":
#         parser = argparse.ArgumentParser(description="Manage your to-do list")
#         parser.add_argument("action", choices=["add", "list", "done"], help="Action to perform")
#         parser.add_argument("--item-text", help="Text of the ite to add")
#         parser.add_argument("--item-number", type=int, help="Number of the item to mark done")
#         args = parser.parse_args()

#         if args.action == "add":
#             add_item(args.item_text)
#         elif args.action == "done":
#             mark_item_done(args.item_number)
#         elif args.action == "list":
#             list_items()
