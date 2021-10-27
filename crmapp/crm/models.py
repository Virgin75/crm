from django.db import models
from django.contrib.auth.models import User

CLIENT_TYPES = [
    (0, 'Lead'),
    (1, 'Customer')
]


class Clients(models.Model):
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


class EventStatus(models.Model):
    status_name = models.CharField(max_length=50)


class Events(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    notes = models.TextField()


class ContractStatus(models.Model):
    status_name = models.CharField(max_length=50)


class Contracts(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    payment_due_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    status = models.ForeignKey(ContractStatus, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
