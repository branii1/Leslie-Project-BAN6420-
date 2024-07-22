# policyholder.py

class Policyholder:
    def __init__(self, name, policy_id):
        self.name = name
        self.policy_id = policy_id
        self.active = True
        self.products = []

    def register_product(self, product):
        self.products.append(product)

    def suspend(self):
        self.active = False

    def reactivate(self):
        self.active = True

    def display_details(self):
        status = "Active" if self.active else "Suspended"
        print(f"Policyholder Name: {self.name}")
        print(f"Policy ID: {self.policy_id}")
        print(f"Status: {status}")
        print("Products:")
        for product in self.products:
            print(f"  - {product.name}")
