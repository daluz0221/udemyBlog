from django.contrib import admin

# Register your models here.
from .models import Contact, Home, Suscribers

admin.site.register(Home)
admin.site.register(Suscribers)
admin.site.register(Contact)