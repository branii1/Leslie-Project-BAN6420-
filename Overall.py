# main.py

from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product("Health Insurance", "P001", 200)
product2 = Product("Life Insurance", "P002", 300)

# Create policyholders
policyholder1 = Policyholder("Alice", "PH001")
policyholder2 = Policyholder("Bob", "PH002")

# Register products to policyholders
policyholder1.register_product(product1)
policyholder2.register_product(product2)

# Create payments
payment1 = Payment(200, "2023-07-13")
payment2 = Payment(300, "2023-07-14")

# Process payments
payment1.process_payment()
payment2.process_payment()

# Display policyholder details
print("Policyholder 1 Details:")
policyholder1.display_details()

print("\nPolicyholder 2 Details:")
policyholder2.display_details()

# Display payment details
print("\nPayment 1 Details:")
payment1.display_details()

print("\nPayment 2 Details:")
payment2.display_details()
