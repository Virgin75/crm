from django.db import models
from django.contrib.auth.models import User

CLIENT_TYPES = [
    ('lead', 'Lead'),
    ('customer', 'Customer')
]


class Clients(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    mobile = models.IntegerField()
    client_type = models.CharField(max_length=10,
                                   choices=CLIENT_TYPES,
                                   default='lead')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE)
