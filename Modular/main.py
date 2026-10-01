"""main.py - MODULAR version (functions split across files, no classes)"""

from menu import display_menu
from inputs import ask_yes_no
from orders import collect_orders, calculate_subtotal
from discount import apply_discount
from receipt import print_receipt


def main():
    print("Welcome to Quick Bite Fast Food Ordering System!")
    display_menu()

    if not ask_yes_no("Would you like to place an order? (Y/N): "):
        print("\nThank you for visiting Quick Bite. Goodbye!")
        return

    customer_orders = collect_orders()
    subtotal = calculate_subtotal(customer_orders)
    discount_label, discount_amount = apply_discount(subtotal)
    final_total = subtotal - discount_amount

    print_receipt(customer_orders, subtotal, discount_label, discount_amount, final_total)


main()