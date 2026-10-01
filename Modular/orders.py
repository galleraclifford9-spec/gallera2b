"""orders.py - collecting orders and computing the subtotal"""

from menu import MENU
from inputs import ask_yes_no, get_valid_menu_item, get_valid_quantity


def collect_orders():
    customer_orders = []
    while True:
        item = get_valid_menu_item()
        quantity = get_valid_quantity()
        price = MENU[item]
        line_total = price * quantity

        customer_orders.append({
            "item": item,
            "quantity": quantity,
            "price": price,
            "line_total": line_total,
        })
        print(f"Added: {quantity} x {item} = P{line_total:.2f}\n")

        if not ask_yes_no("Order another item? (Y/N): "):
            break
    return customer_orders


def calculate_subtotal(customer_orders):
    return sum(order["line_total"] for order in customer_orders)