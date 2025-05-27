from django.db import models

class Transaction(models.Model):
    TransactionChoices = [
        ("INV", "Invoice"),
        ("PAY", "Payment"),
        ("CRD", "Credit Card"),
        ("BNK", "Bank Transfer"),
        ("CSH", "Cash"),
        ("CHK", "Check"),
        ("PPY", "PayPal"),
        ("APP", "Apple Pay"),
        ("GPA", "Google Pay"),
        ("BTC", "Bitcoin"),
        ("OTH", "Other")
    ]

    amount = models.PositiveIntegerField()
    transaction_date = models.DateField()
    transaction_type = models.CharField(
        max_length=255,
        default= "PAY",
        choices=TransactionChoices
    )

    def __str__(self):
        return str(self.amount)