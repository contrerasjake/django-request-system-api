from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
# Create your models here.
class UserInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='profile')
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    CIVIL_STATUS = (       
        ('CIVIL_MARRIED', 'Married'),
        ('CIVIL_SINGLE', 'Single'),
        ('CIVIL_DIVORCED', 'Divorced'),
        ('CIVIL_WIDOWED', 'Widowed'),
    )
    
    PROVINCE_CHOICES = (
        ('Metro Manila', 'Metro Manila'),
        ('Abra', 'Abra'),
        ('Agusan Del Norte', 'Agusan Del Norte'),
        ('Agusan Del Sur', 'Agusan Del Sur'),
        ('Aklan', 'Aklan'),
        ('Albay', 'Albay'),
        ('Antique', 'Antique'),
        ('Apayao', 'Apayao'),
        ('Aurora', 'Aurora'),
        ('Basilan', 'Basilan'),
        ('Bataan', 'Bataan'),
        ('Batanes', 'Batanes'),
        ('Batangas', 'Batangas'),
        ('Benguet', 'Benguet'),
        ('Biliran', 'Biliran'),
        ('Bohol', 'Bohol'),
        ('Bukidnon', 'Bukidnon'),
        ('Bulacan', 'Bulacan'),
        ('Cagayan', 'Cagayan'),
        ('Camarines Norte', 'Camarines Norte'),
        ('Camarines Sur', 'Camarines Sur'),
        ('Camiguin', 'Camiguin'),
        ('Capiz', 'Capiz'),
        ('Catanduanes', 'Catanduanes'),
        ('Cavite', 'Cavite'),
        ('Cebu', 'Cebu'),
        ('Compostella Valley', 'Compostella Valley'),
        ('Cotabato', 'Cotabato'),
        ('Davao Del Norte', 'Davao Del Norte'),
        ('Davao Del Sur', 'Davao Del Sur'),
        ('Davao Occidental', 'Davao Occidental'),
        ('Davao Oriental', 'Davao Oriental'),
        ('Dinagat Islands', 'Dinagat Islands'),
        ('Eastern Samar', 'Eastern Samar'),
        ('Guimaras', 'Guimaras'),
        ('Ifugao', 'Ifugao'),
        ('Ilocos Norte', 'Ilocos Norte'),
        ('Ilocos Sur', 'Ilocos Sur'),
        ('Iloilo', 'Iloilo'),
        ('Isabela', 'Isabela'),
        ('Kalinga', 'Kalinga'),
        ('La Union', 'La Union'),
        ('Laguna', 'Laguna'),
        ('Lanao Del Norte', 'Lanao Del Norte'),
        ('Lanao Del Sur', 'Lanao Del Sur'),
        ('Leyte', 'Leyte'),
        ('Maguindanao', 'Maguindanao'),
        ('Marinduque', 'Marinduque'),
        ('Masbate', 'Masbate'),
        ('Misamis Occidental', 'Misamis Occidental'),
        ('Misamis Oriental', 'Misamis Oriental'),
        ('Mountain Province', 'Mountain Province'),
        ('Negros Occidental', 'Negros Occidental'),
        ('Negros Oriental', 'Negros Oriental'),
        ('Northern Samar', 'Northern Samar'),
        ('Nueva Ecija', 'Nueva Ecija'),
        ('Nueva Vizcaya', 'Nueva Vizcaya'),
        ('Occidental Mindoro', 'Occidental Mindoro'),
        ('Oriental Mindoro', 'Oriental Mindoro'),
        ('Palawan', 'Palawan'),
        ('Pampanga', 'Pampanga'),
        ('Pangasinan', 'Pangasinan'),
        ('Quezon', 'Quezon'),
        ('Quirino', 'Quirino'),
        ('Rizal', 'Rizal'),
        ('Romblon', 'Romblon'),
        ('Samar', 'Samar'),
        ('Sarangani', 'Sarangani'),
        ('Siquijor', 'Siquijor'),
        ('Sorsogon', 'Sorsogon'),
        ('South Cotabato', 'South Cotabato'),
        ('Southern Leyte', 'Southern Leyte'),
        ('Sultan Kudarat', 'Sultan Kudarat'),
        ('Sulu', 'Sulu'),
        ('Surigao Del Norte', 'Surigao Del Norte'),
        ('Surigao Del Sur', 'Surigao Del Sur'),
        ('Tarlac', 'Tarlac'),
        ('Tawi-Tawi', 'Tawi-Tawi'),
        ('Zambales', 'Zambales'),
        ('Zamboanga Del Norte', 'Zamboanga Del Norte'),
        ('Zamboanga Del Sur', 'Zamboanga Del Sur'),
        ('Zamboanga Sibugay', 'Zamboanga Sibugay')
    )
    

    def validate_num(value):
        if value <= 18:
            raise ValidationError(
                _('%(value)s is not a valid number'),
                params={'value': value},
            )
    # UserName = models.CharField(max_length=100, blank=False, default='')
    # FirstName = models.CharField(max_length=100, blank=False)
    # LastName = models.CharField(max_length=100, blank=False)
    MiddleName = models.CharField(max_length=100, blank=False)
    Address = models.CharField(max_length=100, blank=False)
    # Email = models.EmailField(null=True, blank=True, max_length=254)
    MobileNumber = PhoneNumberField(null=False, blank=False, unique=True)
    date_created = models.DateField(auto_now_add=True)
    resident_number=models.CharField(max_length=100, blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null = True, )
    age = models.SmallIntegerField(null=True, validators=[validate_num])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null = True)
    province = models.CharField(max_length=50, blank=False,null = True, choices=PROVINCE_CHOICES)
    civil_status = models.CharField(max_length=50, blank=False, null = True, choices=CIVIL_STATUS)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profilepic/%Y/%m/%D/")
    id_pic = models.ImageField(null=True, blank=True, upload_to="id_pic/%Y/%m/%D/")

    def __str__(self):
        return '{}'.format(self.resident_number)

    

    