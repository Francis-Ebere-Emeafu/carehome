from django.contrib import admin
from accounts.models import Account
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "first_name",
        "last_name",
        "phone",
        "when"
    ]
    # list_filter = ["paid", "membership_email_sent"]
    search_fields = ["first_name", "last_name", "email"]
