import argparse

FILENAME ="todo.txt"

def add_strikethrough(item):
    return f"\xlb[9m{item}\x1b[0m"

def add(item):
    with open(FILENAME, "a") as file:
        file.write(f"{item}\n")
        file.close()
        print(f"Added item: {item}")
        
def list_items():
    lines = None
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{FILENAME}' not found")
    if not lines:
        print("No items found")
    else:
        print(lines)
        for i, line in enumerate(lines):
            print(f"{i+1}, {line.strip()}")
    
    def mark_item_done(item_number):
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("Invalid item number.")
        elif item_number < 1 or item_number > len(lines):
            print("Invalid item number")
            
            item = lines[item_number-1].rstrip()
            item = add_strikethrough(item)
            with open(FILENAME, "w") as file:
                for i, line in enumerate(lines):
                    if i == item_number-1:
                        file.write(f"{item}\n")
                        print(f"Marked item as done: {item}")
                    else:
                        print(line)
                        file.write(line)
            
    