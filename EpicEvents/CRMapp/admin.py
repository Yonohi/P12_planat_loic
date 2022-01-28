from django.contrib import admin
from .models import Client, Contract, Event, UserManagement, UserSale, UserSupport

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
admin.site.register(UserSupport)
admin.site.register(UserSale)
admin.site.register(UserManagement)