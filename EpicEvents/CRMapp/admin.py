from django.contrib import admin
from .models import Client, Contract, Event, EventStatus

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
admin.site.register(EventStatus)


