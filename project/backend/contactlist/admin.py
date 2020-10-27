from django.contrib import admin
from .models import Addresses, ContactGroup
# Register your models here.

@admin.register(ContactGroup)
class ContactgroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)

@admin.register(Addresses)
class ContactlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'created')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'phone_number')
