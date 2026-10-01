"""fast_food.py - all the classes for the OOP version"""

import datetime


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    WIDTH = 40

    def __init__(self, items=None):
        self._items = list(items) if items else []

    def find(self, text):
        """Find an item by number (1-based) or name. Returns MenuItem or None."""
        text = text.strip()
        if text.isdigit():
            index = int(text)
            if 1 <= index <= len(self._items):
                return self._items[index - 1]
            return None
        for item in self._items:
            if item.name.lower() == text.lower():
                return item
        return None

    def display(self):
        print("\n" + "=" * self.WIDTH)
        print(f"{'FAST FOOD MENU':^{self.WIDTH}}")
        print("=" * self.WIDTH)
        print(f"{'#':<4}{'Item':<21}{'Price':>15}")
        print("-" * self.WIDTH)
        for number, item in enumerate(self._items, start=1):
            print(f"{number:<4}{item.name:<21}{'P' + format(item.price, '.2f'):>15}")
        print("=" * self.WIDTH + "\n")


class OrderLine:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    @property
    def unit_price(self):
        return self.menu_item.price

    @property
    def line_total(self):
        return self.menu_item.price * self.quantity


class Discount:
    BULK_THRESHOLD = 500.00
    BULK_RATE = 0.10

    def __init__(self, label="None", amount=0.00):
        self.label = label
        self.amount = amount

    @classmethod
    def for_subtotal(cls, subtotal):
        if subtotal >= cls.BULK_THRESHOLD:
            return cls(f"Bulk Order Discount ({int(cls.BULK_RATE * 100)}%)",
                       subtotal * cls.BULK_RATE)
        return cls()

    @property
    def is_applied(self):
        return self.amount > 0


class Order:
    def __init__(self):
        self.lines = []

    def add_line(self, menu_item, quantity):
        line = OrderLine(menu_item, quantity)
        self.lines.append(line)
        return line

    @property
    def subtotal(self):
        return sum(line.line_total for line in self.lines)

    @property
    def discount(self):
        return Discount.for_subtotal(self.subtotal)

    @property
    def total(self):
        return self.subtotal - self.discount.amount


class Receipt:
    WIDTH = 40

    def __init__(self, order):
        self.order = order

    def print(self):
        w = self.WIDTH
        now = datetime.datetime.now().strftime("%B %d, %Y  %I:%M %p")

        print("\n" + "=" * w)
        print(f"{'FAST FOOD':^{w}}")
        print(f"{'IT Street Road 143, Cebu City':^{w}}")
        print(f"{now:^{w}}")
        print("=" * w)
        print(f"{'Item':<16}{'Qty':>4}{'Price':>9}{'Total':>11}")
        print("-" * w)
        for line in self.order.lines:
            print(f"{line.menu_item.name:<16}{line.quantity:>4}"
                  f"{line.unit_price:>9.2f}{line.line_total:>11.2f}")
        print("-" * w)
        print(f"{'Subtotal:':<29}{self.order.subtotal:>11.2f}")
        d = self.order.discount
        if d.is_applied:
            print(f"{d.label:<29}{'-' + format(d.amount, '.2f'):>11}")
        print(f"{'TOTAL:':<29}{self.order.total:>11.2f}")
        print("=" * w)
        print(f"{'Thank you for your order!':^{w}}")
        print(f"{'Please come again!':^{w}}")
        print("=" * w + "\n")


class InputHelper:
    @staticmethod
    def ask_yes_no(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ("y", "yes"):
                return True
            if response in ("n", "no"):
                return False
            print("Invalid input. Please answer 'Y' for Yes or 'N' for No.")

    @staticmethod
    def ask_menu_item(menu):
        while True:
            typed = input("Enter menu item number or name: ")
            item = menu.find(typed)
            if item:
                return item
            print(f"'{typed.strip()}' is not a valid menu choice. Please try again.")
            print("Tip: enter the item number (e.g., 1) or the exact item name.\n")

    @staticmethod
    def ask_quantity():
        while True:
            typed = input("Enter quantity: ").strip()
            try:
                value = int(typed)
            except ValueError:
                print("Invalid input. Please enter a whole number (e.g., 1, 2, 3).")
                continue
            if value <= 0:
                print("Quantity must be a positive whole number. Try again.")
                continue
            return value


class POSApp:
    def __init__(self):
        self.menu = Menu([
            MenuItem("Cheeseburger", 90.00),
            MenuItem("Chicken Sandwich", 100.00),
            MenuItem("French Fries", 50.00),
            MenuItem("Onion Rings", 65.00),
            MenuItem("Nuggets (6pc)", 95.00),
            MenuItem("Cola (Regular)", 35.00),
            MenuItem("Iced Tea (Regular)", 40.00),
            MenuItem("Sundae", 40.00),
            MenuItem("Apple Pie", 50.00),
        ])

    def collect_order(self):
        order = Order()
        while True:
            item = InputHelper.ask_menu_item(self.menu)
            quantity = InputHelper.ask_quantity()
            line = order.add_line(item, quantity)
            print(f"Added: {line.quantity} x {item.name} = P{line.line_total:.2f}\n")
            if not InputHelper.ask_yes_no("Order another item? (Y/N): "):
                break
        return order

    def run(self):
        print("Welcome to Quick Bite Fast Food Ordering System!")
        self.menu.display()

        if not InputHelper.ask_yes_no("Would you like to place an order? (Y/N): "):
            print("\nThank you for visiting Quick Bite. Goodbye!")
            return

        order = self.collect_order()
        Receipt(order).print()