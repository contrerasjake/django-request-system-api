from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserInformation(models.Model):
    FirstName = models.CharField(max_length=100, blank=False)
    LastName = models.CharField(max_length=100, blank=False)
    MiddleName = models.CharField(max_length=100, blank=False)
    Address = models.CharField(max_length=100, blank=False)
    Email = models.EmailField(null=True, blank=True, max_length=254)
    MobileNumber = PhoneNumberField(null=False, blank=False, unique=True)
    date_created = models.DateField(auto_now_add=True)
    resident_number=models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {} , {}'.format(self.FirstName, self.LastName, self.resident_number)