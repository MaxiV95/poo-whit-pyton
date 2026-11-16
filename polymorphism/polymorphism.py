class CreditCard:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def process_payment(self) -> None:
        print(f"Processing payment of {self.amount} {self.currency} with credit card.")

class PayPal:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def process_payment(self) -> None:
        print(f"Processing payment of {self.amount} {self.currency} via PayPal.")

payment_methods: list[CreditCard | PayPal] = [
    CreditCard(100, "USD"),
    PayPal(200, "EUR"),
    CreditCard(50, "GBP"),
    PayPal(75, "USD")
    ]

for method in payment_methods:
    method.process_payment()