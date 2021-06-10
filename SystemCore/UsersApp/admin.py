from django.contrib import admin
from .models import UserInformation

# Register your models here.
class formsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Personal Details", {
            "fields": (
                'FirstName', 'LastName', 'MiddleName','resident_number', 'Address', 'date_of_birth', 'age', 'gender', 'province', 'civil_status'
            )
        }),
        ("Contact Details", {
            "fields": (
                'Email', 'MobileNumber'
            )
        })
    )
    search_fields = ['FirstName', 'LastName', 'resident_number']
    list_display = ('resident_number', 'FirstName', 'LastName', 'MiddleName', 'Address', 'Email', 'MobileNumber', 'date_created')
admin.site.register(UserInformation, formsAdmin)