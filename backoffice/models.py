from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Bank(models.Model):
    TYPES_OF_BANKS = [
        ('PRI', 'Private'),
        ('PUB', 'Public')
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    type = models.CharField(
        max_length=3,
        choices=TYPES_OF_BANKS,
        null=True,
        default=None
        )
    
    def __str__(self):
        return self.name




class Client(models.Model):
    TYPES_OF_CLIENTS = [
        ('N', 'Natural'),
        ('J', 'Juridico')
    ]

    name = models.CharField(max_length=60)
    birthday = models.DateField(default=None)
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(1), MaxValueValidator(99)])
    nationality = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    type = models.CharField(
        max_length=1,
        choices=TYPES_OF_CLIENTS,
        default='N'
    )
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





class Credit(models.Model):
    TYPES_OF_CREDITS = [
        ('AUT', 'Automotriz'),
        ('HIP', 'Hipotecarios'),
        ('COM', 'Comerciales')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    minPayment = models.DecimalField(max_digits=15, decimal_places=2)
    maxPayment = models.DecimalField(max_digits=15, decimal_places=2)
    creditMonths = models.IntegerField()
    registryDate = models.DateField(auto_now_add=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=3,
        choices=TYPES_OF_CREDITS,
        null=True,
        default=None
    )

    def __str__(self):
        return self.client.name