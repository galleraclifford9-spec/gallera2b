"""receipt.py - receipt printing"""

import datetime


def print_receipt(customer_orders, subtotal, discount_label, discount_amount, final_total):
    now = datetime.datetime.now().strftime("%B %d, %Y  %I:%M %p")

    print("\n" + "=" * 40)
    print(f"{'FAST FOOD':^40}")
    print(f"{'IT Street Road 143, Cebu City':^40}")
    print(f"{now:^40}")
    print("=" * 40)
    print(f"{'Item':<16}{'Qty':>4}{'Price':>9}{'Total':>11}")
    print("-" * 40)

    for order in customer_orders:
        print(f"{order['item']:<16}{order['quantity']:>4}"
              f"{order['price']:>9.2f}{order['line_total']:>11.2f}")

    print("-" * 40)
    print(f"{'Subtotal:':<29}{subtotal:>11.2f}")
    if discount_amount > 0:
        print(f"{discount_label:<29}{'-' + format(discount_amount, '.2f'):>11}")
    print(f"{'TOTAL:':<29}{final_total:>11.2f}")
    print("=" * 40)
    print(f"{'Thank you for your order!':^40}")
    print(f"{'Please come again!':^40}")
    print("=" * 40 + "\n")