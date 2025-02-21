from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.user.forms import CustomEmailForm
from .models import UserAccount
from allauth.account.models import EmailAddress

# Register your models here.
class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("email", "first_name", "last_name", "password1", "password2"),},
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)
    readonly_fields = ['date_joined', 'last_login']

class CustomEmailAdmin(admin.ModelAdmin):
    # Override or add fields, filters, etc. for the admin form
    form = CustomEmailForm
    list_display = ('email', 'user', 'verified', 'primary')
    search_fields = ['email', 'user__username']

admin.site.register(UserAccount, UserAdminCustom)
if admin.site.is_registered(EmailAddress):
    admin.site.unregister(EmailAddress)
    admin.site.register(EmailAddress, CustomEmailAdmin)