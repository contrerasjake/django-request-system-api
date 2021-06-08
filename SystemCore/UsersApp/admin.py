from django.contrib import admin
from .models import UserInformation

# Register your models here.
class formsAdmin(admin.ModelAdmin):
    search_fields = ['FirstName', 'LastName', 'resident_number']
    list_display = ('FirstName', 'LastName', 'resident_number', 'MiddleName', 'Address', 'Email', 'MobileNumber', 'date_created')
admin.site.register(UserInformation, formsAdmin)