"""Cart functions for the food ordering app."""
from ordering import MENU, calculate_order_total


class Cart:
    def __init__(self, items=None):
        self.items = dict(items or {})

    def add_item(self, name, qty=1):
        if name not in MENU:
            raise ValueError(f"{name} is not on the menu")
        if qty <= 0:
            raise ValueError("quantity must be positive")
        self.items[name] = self.items.get(name, 0) + qty

    def remove_item(self, name):
        self.items.pop(name, None)

    def update_quantity(self, name, qty):
        if name not in self.items:
            raise ValueError(f"{name} is not in the cart")
        if qty <= 0:
            self.remove_item(name)
        else:
            self.items[name] = qty

    def subtotal(self):
        return sum(MENU[name] * qty for name, qty in self.items.items())

    def total(self, discount_percent=0):
        return calculate_order_total(self.subtotal(), discount_percent)


if __name__ == "__main__":
    cart = Cart()
    cart.add_item("pizza", 2)
    cart.add_item("coke")
    print("Cart:", cart.items, "| Total:", cart.total(10))
