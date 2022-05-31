from django.contrib import admin
from Forms.models import (
    Cedula, 
    BuildingClearance, 
    ConstituentID, 
    Residency, 
    BarangayClearance, 
    Comelec, 
    BusinessClosure, 
    BailBond, 
    Guardianship, 
    IndigencyBurial, 
    IndigencyClearance, 
    Voucher, 
    BusinessClearance, 
    Immunization, 
    DentalService, 
    MaternalCare

)


# Register your models here.
class paidformsAdmin(admin.ModelAdmin):
    search_fields = ['request_number']
    list_display = ('request_number', 'resident_number', 'status', 'date_requested')
    def __unicode__(self):
        return self.name
class formsAdmin(admin.ModelAdmin):
    search_fields = ['request_number']
    list_display = ('request_number', 'resident_number', 'status')

#paid
admin.site.register(Cedula,paidformsAdmin)
admin.site.register(ConstituentID, paidformsAdmin)
admin.site.register(BarangayClearance,paidformsAdmin)
admin.site.register(BailBond,paidformsAdmin)



#not
admin.site.register(BuildingClearance, formsAdmin)
admin.site.register(Residency, formsAdmin)
admin.site.register(Comelec, formsAdmin)
admin.site.register(BusinessClosure, formsAdmin)
admin.site.register(Guardianship, formsAdmin)
admin.site.register(IndigencyBurial, formsAdmin)
admin.site.register(IndigencyClearance, formsAdmin)
admin.site.register(Voucher, formsAdmin)
admin.site.register(BusinessClearance, formsAdmin)
admin.site.register(Immunization, formsAdmin)
admin.site.register(DentalService, formsAdmin)
admin.site.register(MaternalCare, formsAdmin)