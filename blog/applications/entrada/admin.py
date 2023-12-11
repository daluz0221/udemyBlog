from django.contrib import admin

# Register your models here.
from .models import Category, Entry,Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry)