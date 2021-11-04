from django.contrib import admin
from crm.models import ContractStatus, Contract, EventStatus, Event, Client

# Register your models here.

admin.site.register(Contract)
admin.site.register(ContractStatus)
admin.site.register(Event)
admin.site.register(EventStatus)
admin.site.register(Client)
