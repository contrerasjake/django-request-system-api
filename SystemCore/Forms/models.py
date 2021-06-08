from django.db import models
from django.db.models import fields
from UsersApp.models import UserInformation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_num(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a valid number'),
            params={'value': value},
        )

class Cedula(models.Model):
    
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    birth_place = models.CharField(max_length = 100, blank=False)
    profession = models.CharField(max_length = 100, null=True, blank=True)
    monthly_income = models.PositiveIntegerField(default=0, blank=True)
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

class BuildingClearance(models.Model):
    
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    maintenance_type = models.CharField(max_length=100, blank=False)
    approval = models.BooleanField(default=False)

class ConstituentID(models.Model):
    
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE,)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    id_number = models.PositiveIntegerField(default=0, blank=False, unique=True)
    date_received = models.DateField(blank=False)
    signature = models.ImageField(blank=False, null=True, upload_to="signature/%Y/%m/%D/")
    picture = models.ImageField(blank=False, null=True, upload_to="pic/%Y/%m/%D/")
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

class Residency(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    approval = models.BooleanField(default=False)

class BarangayClearance(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    has_payment = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

class Comelec(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    approval = models.BooleanField(default=False)

class BusinessClosure(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    business_name = models.CharField(max_length=100, blank=False)
    business_owner = models.CharField(max_length=100, blank=False)
    business_address = models.CharField(max_length=100, blank=False)
    business_nature = models.CharField(max_length=100, blank=False)
    last_business_operated = models.DateField(blank=False)
    approval = models.BooleanField(default=False)

class BailBond(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    case_number = models.PositiveIntegerField(default=0, unique=True)
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)


class Guardianship(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    guardian_name = models.CharField(max_length = 100, blank=False)
    approval = models.BooleanField(default=False)


class IndigencyBurial(models.Model):
    
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    deceased_relationship = models.CharField(max_length = 100, blank=False)
    deceased_name = models.CharField(max_length = 100, blank=False)
    passed_onto_whom = models.CharField(max_length = 100, blank=False)
    approval = models.BooleanField(default=False)

class IndigencyClearance(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    patient_relationship = models.CharField(max_length = 100, blank=False)
    patient_name = models.CharField(max_length = 100, blank=False)
    purpose = models.CharField(max_length = 100, blank=False)
    passed_onto_whom = models.CharField(max_length = 100, blank=False)
    approval = models.BooleanField(default=False)

class Voucher(models.Model):

    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    student_name = models.CharField(max_length = 100, blank=False)
    parent_name = models.CharField(max_length = 100, blank=False)
    school = models.CharField(max_length = 100, blank=False)
    grade = models.PositiveIntegerField(default=0, blank=False)
    approval = models.BooleanField(default=False)


class BusinessClearance(models.Model):
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    business_name = models.CharField(max_length=100, blank=False)
    business_owner = models.CharField(max_length=100, blank=False)
    business_address = models.CharField(max_length=100, blank=False)
    business_nature = models.CharField(max_length=100, blank=False)
    start_business_operated = models.DateField(blank=False)
    approval = models.BooleanField(default=False)

class Immunization(models.Model):
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    mother_name = models.CharField(max_length=100, blank=False)
    father_name = models.CharField(max_length=100, blank=False)
    birth_height = models.PositiveIntegerField(default=0, blank=False)
    birth_weight = models.PositiveIntegerField(default=0, blank=False)
    approval = models.BooleanField(default=False)

class DentalService(models.Model):
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    approval = models.BooleanField(default=False)

class MaternalCare(models.Model):
    resident_number = models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(default=0, blank=False,unique=True, validators=[validate_num])
    child_name = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField(blank=False)
    birth_place = models.CharField(max_length=100, blank=False)
    approval = models.BooleanField(default=False)

