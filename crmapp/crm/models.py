from django.db import models
from django.contrib.auth.models import User

CLIENT_TYPES = [
    (0, 'Lead'),
    (1, 'Customer')
]


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    mobile = models.IntegerField()
    client_type = models.PositiveSmallIntegerField(choices=CLIENT_TYPES,
                                                   default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.client_type}'


class EventStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.status_name}'


class Event(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    attendees = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return f'{self.name}, le {self.date}'


class ContractStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.status_name}'


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_due_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    status = models.ForeignKey(ContractStatus, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Contrat de {self.amount} € du client {self.client}'
