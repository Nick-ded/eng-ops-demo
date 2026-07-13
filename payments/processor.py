"""
Payment processor — handles checkout order totals.
Known bug: divide-by-zero when discount_code is None (issue #203).
"""


def calculate_total(order_total: float, discount_code: str | None) -> float:
    """
    Calculate final order total after applying discount.
    BUG: crashes with ZeroDivisionError when discount_code is None.
    """
    discount = order_total / discount_code  # BUG: should be a lookup, not divide
    return order_total - discount


def process_payment(amount: float, card_token: str) -> dict:
    """Stub payment processing — replace with real payment gateway."""
    if not card_token:
        raise ValueError("Card token is required")
    return {"status": "success", "amount": amount, "token": card_token}
