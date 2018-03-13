from django.contrib import admin
from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)

