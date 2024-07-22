# product.py

class Product:
    def __init__(self, name, product_id, price):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.active = True

    def update_product(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price

    def suspend(self):
        self.active = False

    def display_details(self):
        status = "Active" if self.active else "Suspended"
        print(f"Product Name: {self.name}")
        print(f"Product ID: {self.product_id}")
        print(f"Price: ${self.price}")
        print(f"Status: {status}")
