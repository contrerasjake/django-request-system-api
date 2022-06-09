from django.db import models
from django.db.models import fields
from UsersApp.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
# Create your models here.



class Cedula(models.Model):
    
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    birth_place = models.CharField(max_length = 100, blank=False)
    profession = models.CharField(max_length = 100, null=True, blank=True)
    monthly_income = models.CharField(max_length = 100, null=True, blank=True)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Cedula")


class BuildingClearance(models.Model):
    
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    maintenance_type = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Building Clearance")

class ConstituentID(models.Model):
    
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE,)
    request_number = models.AutoField(primary_key=True)
    id_number = models.CharField(max_length = 100, null=True, blank=True)
    date_received = models.DateField(blank=False)
    signature = CloudinaryField('image', blank=False, null=True, folder="constituent/signature")
    picture = CloudinaryField('image', blank=False, null=True, folder="constituent/pic")
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Constituent ID")

class Residency(models.Model):

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Residency")

class BarangayClearance(models.Model):
    PURPOSE_LOAN = 'Loan'
    OTHERS = 'Others'

    PURPOSE = (
        (PURPOSE_LOAN, 'Loan'),
        (OTHERS, 'Others'),
    )

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    purpose = models.CharField(max_length=10, blank=False, null = True, choices=PURPOSE)
    has_payment = models.BooleanField(default=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Barangay Clearance")
    

class Comelec(models.Model):

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Comelec")

class BusinessClosure(models.Model):

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100, blank=False)
    business_owner = models.CharField(max_length=100, blank=False)
    business_address = models.CharField(max_length=100, blank=False)
    business_nature = models.CharField(max_length=100, blank=False)
    last_business_operated = models.DateField(blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Business Closure")

class BailBond(models.Model):

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE, default = None)
    request_number = models.AutoField(primary_key=True)
    case_number = models.CharField(max_length = 100, null=True, blank=True)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Bail Bond")

class Guardianship(models.Model):

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    guardian_name = models.CharField(max_length = 100, blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Guardianship")


class IndigencyBurial(models.Model):
    R_FATHER = 'Father'
    R_MOTHER = 'Mother'
    R_SON = 'Son'
    R_DAUGHTER = 'Daughter'
    OTHERS = 'Others'

    RELATIONSHIP = (
        (R_FATHER, 'Father'),
        (R_MOTHER, 'Mother'),
        (R_SON, 'Son'),
        (R_DAUGHTER, 'Daughter'),
        (OTHERS, 'Others'),
    )

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    deceased_relationship = models.CharField(max_length = 100, blank=False, choices=RELATIONSHIP)
    deceased_name = models.CharField(max_length = 100, blank=False)
    passed_onto_whom = models.CharField(max_length = 100, blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Indigency Burial")

class IndigencyClearance(models.Model):
    # R_FATHER = 'Father'
    # R_MOTHER = 'Mother'
    # R_SON = 'Son'
    # R_DAUGHTER = 'Daughter'
    # OTHERS = 'Others'

    # RELATIONSHIP = (
    #     (R_FATHER, 'Father'),
    #     (R_MOTHER, 'Mother'),
    #     (R_SON, 'Son'),
    #     (R_DAUGHTER, 'Daughter'),
    #     (OTHERS, 'Others'),
    # )

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    # patient_relationship = models.CharField(max_length = 100, blank=False, choices=RELATIONSHIP)
    patient_relationship = models.CharField(max_length = 100, blank=False)
    patient_name = models.CharField(max_length = 100, blank=False)
    purpose = models.CharField(max_length = 100, blank=False)
    passed_onto_whom = models.CharField(max_length = 100, blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Indigency Clearance")

class Voucher(models.Model):

    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length = 100, blank=False)
    parent_name = models.CharField(max_length = 100, blank=False)
    school = models.CharField(max_length = 100, blank=False)
    grade = models.CharField(max_length = 100, blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Voucher")


class BusinessClearance(models.Model):
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100, blank=False)
    business_owner = models.CharField(max_length=100, blank=False)
    business_address = models.CharField(max_length=100, blank=False)
    business_nature = models.CharField(max_length=100, blank=False)
    start_business_operated = models.DateField(blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Business Clearance")

class Immunization(models.Model):
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    mother_name = models.CharField(max_length=100, blank=False)
    father_name = models.CharField(max_length=100, blank=False)
    birth_height = models.FloatField(default=0, blank=False)
    models.CharField(max_length = 100, null=True, blank=True)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Immunization")

class DentalService(models.Model):
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Dental Service")

class MaternalCare(models.Model):
    resident_number = models.ForeignKey(to=User, to_field="resident_number", on_delete=models.CASCADE)
    request_number = models.AutoField(primary_key=True)
    child_name = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField(blank=False)
    birth_place = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length = 100, blank=False, default="Pending")
    date_requested = models.DateField(verbose_name="date requested", auto_now_add=True)
    document_name = models.CharField(max_length = 100, blank=False, default="Maternal Care")

