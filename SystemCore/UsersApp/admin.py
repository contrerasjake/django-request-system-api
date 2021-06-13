from django.contrib import admin
from .models import UserInformation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserInformation

class UserProfileInline(admin.StackedInline):
    model = UserInformation
    can_delete = False

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    inlines = (UserProfileInline, )
# # Register your models here.
# class formsAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ("Personal Details", {
#             "fields": (
#                 'FirstName', 'LastName', 'MiddleName','resident_number', 'Address', 'date_of_birth', 'age', 'gender', 'province', 'civil_status'
#             )
#         }),
#         ("Contact Details", {
#             "fields": (
#                 'Email', 'MobileNumber'
#             )
#         })
#     )
#     search_fields = ['FirstName', 'LastName', 'resident_number']
#     list_display = ('resident_number', 'FirstName', 'LastName', 'MiddleName', 'Address', 'Email', 'MobileNumber', 'date_created')
# admin.site.register(UserInformation, formsAdmin)