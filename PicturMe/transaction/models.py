from django.db import models

class TransactionModel(models.Model):
    class TransactionChoice(models.TextChoices):
        INVOICE = "Invoice", "Invoice"
        PAYMENT = "Payment", "Payment"

    transaction_id = models.IntegerField(primary_key=True)
    amount = models.PositiveIntegerField()
    transaction_date = models.DateField()
    transaction_type = models.CharField(
        max_length=20,
        choices=TransactionChoice.choices
    )