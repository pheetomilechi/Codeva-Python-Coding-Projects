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