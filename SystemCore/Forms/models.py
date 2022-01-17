from django.db import models
from django.db.models import fields
from UsersApp.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.



class Cedula(models.Model):
    
    resident_number = models.ForeignKey(User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    birth_place = models.CharField(max_length = 100, blank=False)
    profession = models.CharField(max_length = 100, null=True, blank=True)
    monthly_income = models.PositiveIntegerField(default=0, blank=True)
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

class BuildingClearance(models.Model):
    
    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    maintenance_type = models.CharField(max_length=100, blank=False)
    approval = models.BooleanField(default=False)

class ConstituentID(models.Model):
    
    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE,)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    id_number = models.PositiveIntegerField(default=0, blank=False, unique=True)
    date_received = models.DateField(blank=False)
    signature = models.ImageField(blank=False, null=True, upload_to="signature/%Y/%m/%D/")
    picture = models.ImageField(blank=False, null=True, upload_to="pic/%Y/%m/%D/")
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

class Residency(models.Model):

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    approval = models.BooleanField(default=False)

class BarangayClearance(models.Model):
    PURPOSE_LOAN = 'Loan'
    OTHERS = 'Others'

    PURPOSE = (
        (PURPOSE_LOAN, 'Loan'),
        (OTHERS, 'Others'),
    )

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    purpose = models.CharField(max_length=10, blank=False, null = True, choices=PURPOSE)
    has_payment = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

    

class Comelec(models.Model):

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    approval = models.BooleanField(default=False)

class BusinessClosure(models.Model):

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    business_name = models.CharField(max_length=100, blank=False)
    business_owner = models.CharField(max_length=100, blank=False)
    business_address = models.CharField(max_length=100, blank=False)
    business_nature = models.CharField(max_length=100, blank=False)
    last_business_operated = models.DateField(blank=False)
    approval = models.BooleanField(default=False)

class BailBond(models.Model):

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    case_number = models.PositiveIntegerField(default=0, unique=True)
    is_paid = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)


class Guardianship(models.Model):

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    guardian_name = models.CharField(max_length = 100, blank=False)
    approval = models.BooleanField(default=False)


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

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    deceased_relationship = models.CharField(max_length = 100, blank=False, choices=RELATIONSHIP)
    deceased_name = models.CharField(max_length = 100, blank=False)
    passed_onto_whom = models.CharField(max_length = 100, blank=False)
    approval = models.BooleanField(default=False)

class IndigencyClearance(models.Model):
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

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    patient_relationship = models.CharField(max_length = 100, blank=False, choices=RELATIONSHIP)
    patient_name = models.CharField(max_length = 100, blank=False)
    purpose = models.CharField(max_length = 100, blank=False)
    passed_onto_whom = models.CharField(max_length = 100, blank=False)
    approval = models.BooleanField(default=False)

class Voucher(models.Model):

    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    student_name = models.CharField(max_length = 100, blank=False)
    parent_name = models.CharField(max_length = 100, blank=False)
    school = models.CharField(max_length = 100, blank=False)
    grade = models.PositiveIntegerField(default=0, blank=False)
    approval = models.BooleanField(default=False)


class BusinessClearance(models.Model):
    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    business_name = models.CharField(max_length=100, blank=False)
    business_owner = models.CharField(max_length=100, blank=False)
    business_address = models.CharField(max_length=100, blank=False)
    business_nature = models.CharField(max_length=100, blank=False)
    start_business_operated = models.DateField(blank=False)
    approval = models.BooleanField(default=False)

class Immunization(models.Model):
    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    mother_name = models.CharField(max_length=100, blank=False)
    father_name = models.CharField(max_length=100, blank=False)
    birth_height = models.PositiveIntegerField(default=0, blank=False)
    birth_weight = models.PositiveIntegerField(default=0, blank=False)
    approval = models.BooleanField(default=False)

class DentalService(models.Model):
    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    approval = models.BooleanField(default=False)

class MaternalCare(models.Model):
    resident_number = models.ForeignKey(to=User, on_delete=models.CASCADE)
    request_number = models.CharField(max_length = 100, blank=False,unique=True)
    child_name = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField(blank=False)
    birth_place = models.CharField(max_length=100, blank=False)
    approval = models.BooleanField(default=False)

