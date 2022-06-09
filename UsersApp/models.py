from email.policy import default
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from cloudinary.models import CloudinaryField
import uuid
import os

def upload_profilepic(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()), ext)
    return os.path.join('uploads/profile_pic', filename)

def upload_idpic(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()), ext)
    return os.path.join('uploads/id_pic', filename)

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, middle_name, last_name, address, mobile_number, resident_number, date_of_birth, age, gender, province, civil_status, profile_pic, id_pic, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not first_name:
            raise ValueError("User must have a last name.")
        if not last_name:
            raise ValueError("User must have a last name.")
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            middle_name = middle_name,
            address = address,
            mobile_number = mobile_number,
            resident_number = resident_number,
            date_of_birth = date_of_birth,
            age = age,
            gender = gender,
            province = province,
            civil_status = civil_status,
            profile_pic = profile_pic,
            id_pic = id_pic,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            middle_name = '',
            last_name = last_name,
            address = '',
            mobile_number = None,
            resident_number = None,
            date_of_birth = None,
            age = None,
            gender = None,
            province = None,
            civil_status = None,
            profile_pic = None,
            id_pic = None,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_email_verified = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )
    CIVIL_STATUS = (       
        ('MARRIED', 'Married'),
        ('SINGLE', 'Single'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
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
    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined             = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name="last login", auto_now=True, null=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_email_verified       = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    first_name              = models.CharField(max_length=100, blank=False)
    middle_name              = models.CharField(max_length=100, blank=True)
    last_name                = models.CharField(max_length=100, blank=False)
    address                 = models.CharField(max_length=100, blank=False)
    mobile_number            = PhoneNumberField(null=True, blank=False, unique=True)
    resident_number         = models.CharField(max_length=100, blank=False, null=True, unique=True)
    date_of_birth           = models.DateField(blank=False, null = True, )
    age                     = models.SmallIntegerField(null=True, validators=[validate_num])
    gender                  = models.CharField(max_length=10, choices=GENDER_CHOICES, null = True)
    province                = models.CharField(max_length=50, blank=False,null = True)
    civil_status            = models.CharField(max_length=50, blank=False, null = True, choices=CIVIL_STATUS)
    profile_pic             = CloudinaryField('image', null=True, blank=True, folder=upload_profilepic)
    id_pic                  = CloudinaryField('image', null=True, blank=True, folder=upload_idpic)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return '{}'.format(self.resident_number)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True