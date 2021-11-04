from django.contrib import admin
from crm.models import ContractStatus, Contracts, EventStatus, Events, Clients

# Register your models here.

admin.site.register(Contracts)
admin.site.register(ContractStatus)
admin.site.register(Events)
admin.site.register(EventStatus)
admin.site.register(Clients)
