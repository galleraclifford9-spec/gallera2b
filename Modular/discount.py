"""discount.py - discount rules"""

BULK_DISCOUNT_THRESHOLD = 500.00
BULK_DISCOUNT_RATE = 0.10


def apply_discount(subtotal):
    label = "None"
    amount = 0.00
    if subtotal >= BULK_DISCOUNT_THRESHOLD:
        label = "Bulk Order Discount (10%)"
        amount = subtotal * BULK_DISCOUNT_RATE
    return label, amount