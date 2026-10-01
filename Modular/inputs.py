"""inputs.py - validated user input"""

from menu import MENU


def ask_yes_no(prompt_message):
    while True:
        response = input(prompt_message).strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        print("Invalid input. Please answer 'Y' for Yes or 'N' for No.")


def get_valid_menu_item():
    number_lookup = {str(i): name for i, name in enumerate(MENU, start=1)}
    lowercase_lookup = {name.lower(): name for name in MENU}

    while True:
        typed = input("Enter menu item number or name: ").strip()
        if typed in number_lookup:
            return number_lookup[typed]
        elif typed.lower() in lowercase_lookup:
            return lowercase_lookup[typed.lower()]
        print(f"'{typed}' is not a valid menu choice. Please try again.")
        print("Tip: enter the item number (e.g., 1) or the exact item name.\n")


def get_valid_quantity():
    while True:
        typed = input("Enter quantity: ").strip()
        try:
            value = int(typed)
            if value <= 0:
                print("Quantity must be a positive whole number. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 1, 2, 3).")