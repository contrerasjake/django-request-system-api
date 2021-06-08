from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


# Create your models here.
class UserInformation(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'

    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )
    CIVIL_MARRIED = 'Ma'
    CIVIL_SINGLE = 'Single'
    CIVIL_DIVORCED ='Divorced'
    CIVIL_WIDOWED = 'Widowed'

    CIVIL_STATUS = (       
        (CIVIL_MARRIED, 'Married'),
        (CIVIL_SINGLE, 'Single'),
        (CIVIL_DIVORCED, 'Divorced'),
        (CIVIL_WIDOWED, 'Widowed'),
    )
    def validate_num(value):
        if value <= 18:
            raise ValidationError(
                _('%(value)s is not a valid number'),
                params={'value': value},
            )

    FirstName = models.CharField(max_length=100, blank=False)
    LastName = models.CharField(max_length=100, blank=False)
    MiddleName = models.CharField(max_length=100, blank=False)
    Address = models.CharField(max_length=100, blank=False)
    Email = models.EmailField(null=True, blank=True, max_length=254)
    MobileNumber = PhoneNumberField(null=False, blank=False, unique=True)
    date_created = models.DateField(auto_now_add=True)
    resident_number=models.CharField(max_length=100, blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null = True, )
    age = models.SmallIntegerField(null=True, validators=[validate_num])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null = True)
    province = models.CharField(max_length=100, blank=False,null = True)
    civil_status = models.CharField(max_length=10, blank=False, null = True, choices=CIVIL_STATUS)
    
    

    

    def __str__(self):
        return '{} {} , {}'.format(self.FirstName, self.LastName, self.resident_number)