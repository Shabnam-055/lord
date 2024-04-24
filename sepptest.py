class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity, price):
        self.items[item_name] = (self.items.get(item_name, 0) + quantity, price)
    def delete_item(self, item_name):
        del self.items[item_name]
    def update_item(self, item_name, quantity, price):
        self.items[item_name] = (quantity, price)
    def display_cart(self):
        total_amount = sum(quantity * price for quantity, price in self.items.values())
        print("Shopping Cart:")
        for item_name, (quantity, price) in self.items.items():
            print(f"{item_name}: Quantity - {quantity}, Price - ${price}, Total - ${quantity * price}")
        print(f"Total Amount: ${total_amount}")
cart = ShoppingCart()
cart.add_item("Apple", 3, 1.5)
cart.add_item("Banana", 2, 0.75)
cart.add_item("Orange", 1, 2.0)
cart.display_cart()
cart.update_item("Apple", 5, 1.75)
cart.display_cart()
cart.delete_item("Banana")
cart.display_cart()
