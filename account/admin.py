from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomerUser


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info",{"fields": ("phone",)}),
    )



