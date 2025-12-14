import random
from django.db import models
from django.conf import settings

class Payment(models.Model):

    PAYMENT_MODE_CHOICES = (
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    )

    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    )

    transaction_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='paid')

    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = self.generate_transaction_id()
        super().save(*args, **kwargs)

    def generate_transaction_id(self):
        while True:
            txn_id = f"TXN-{random.randint(1000, 9999)}"
            if not Payment.objects.filter(transaction_id=txn_id).exists():
                return txn_id

    def __str__(self):
        return self.transaction_id
