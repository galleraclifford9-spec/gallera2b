"""menu.py - menu data and display"""

MENU = {
    "Cheeseburger": 90.00,
    "Chicken Sandwich": 100.00,
    "French Fries": 50.00,
    "Onion Rings": 65.00,
    "Nuggets (6pc)": 95.00,
    "Cola (Regular)": 35.00,
    "Iced Tea (Regular)": 40.00,
    "Sundae": 40.00,
    "Apple Pie": 50.00,
}


def display_menu():
    print("\n" + "=" * 40)
    print(f"{'FAST FOOD MENU':^40}")
    print("=" * 40)
    print(f"{'#':<4}{'Item':<21}{'Price':>15}")
    print("-" * 40)
    for number, (name, price) in enumerate(MENU.items(), start=1):
        print(f"{number:<4}{name:<21}{'P' + format(price, '.2f'):>15}")
    print("=" * 40 + "\n")