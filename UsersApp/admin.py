from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from .models import User

class userAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, userAdmin)