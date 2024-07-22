# payment.py

class Payment:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date
        self.paid = False

    def process_payment(self):
        self.paid = True

    def display_details(self):
        status = "Paid" if self.paid else "Unpaid"
        print(f"Payment Amount: ${self.amount}")
        print(f"Payment Date: {self.date}")
        print(f"Status: {status}")
