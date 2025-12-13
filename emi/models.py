from django.db import models
from products.models import Product

class Bank(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='banks/', null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Annual Interest Rate in %")
    
    def __str__(self):
        return self.name

class EMIApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    )
    
    application_no = models.CharField(max_length=50, unique=True, editable=False)
    
    # Customer Details
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    dob = models.DateField()
    national_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, blank=True)
    marital_status = models.CharField(max_length=20, blank=True)
    monthly_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    # Product & Loan Details
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='emi_applications')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    down_payment = models.DecimalField(max_digits=12, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tenure = models.PositiveIntegerField(help_text="Duration in months")
    monthly_emi = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Bank Details
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)
    bank_account_no = models.CharField(max_length=50)
    card_last_four = models.CharField(max_length=4)
    
    # Guarantor Details
    guarantor_name = models.CharField(max_length=255, blank=True)
    guarantor_phone = models.CharField(max_length=20, blank=True)
    guarantor_national_id = models.CharField(max_length=50, blank=True)
    guarantor_address = models.TextField(blank=True)
    
    # Documents
    user_photo = models.ImageField(upload_to='emi_docs/user/', null=True, blank=True)
    citizenship_front = models.ImageField(upload_to='emi_docs/id/', null=True, blank=True)
    citizenship_back = models.ImageField(upload_to='emi_docs/id/', null=True, blank=True)
    bank_statement = models.ImageField(upload_to='emi_docs/bank/', null=True, blank=True)
    guarantor_photo = models.ImageField(upload_to='emi_docs/guarantor/', null=True, blank=True)
    guarantor_citizenship_front = models.ImageField(upload_to='emi_docs/guarantor/', null=True, blank=True)
    guarantor_citizenship_back = models.ImageField(upload_to='emi_docs/guarantor/', null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.application_no:
            import uuid
            self.application_no = f"EMI-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.application_no} - {self.customer_name}"
