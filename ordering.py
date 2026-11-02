"""Order total calculation for the food ordering app."""

MENU = {
    "pizza": 250.0,
    "burger": 120.0,
    "pasta": 180.0,
    "coke": 40.0,
}


def calculate_order_total(subtotal, discount_percent=0):
    """Return the order total after applying a percentage discount.

    Raises ValueError for a negative subtotal or a discount outside 0-100.
    """
    if not isinstance(subtotal, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise TypeError("subtotal and discount_percent must be numbers")
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount must be between 0 and 100")
    return round(subtotal - subtotal * discount_percent / 100, 2)


if __name__ == "__main__":
    order = {"pizza": 2, "coke": 3}
    subtotal = sum(MENU[item] * qty for item, qty in order.items())
    print("Order:", order)
    print(f"Subtotal: Rs {subtotal:.2f}")
    print(f"Total with 10% discount: Rs {calculate_order_total(subtotal, 10):.2f}")
