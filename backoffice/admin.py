from django.contrib import admin
from .models import Bank, Client, Credit

admin.site.register(Bank)
admin.site.register(Client)
admin.site.register(Credit)
