from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class CedulaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cedula
        exclude = ['resident_number']
                
class BuildingClearanceSerializer(ModelSerializer):

    class Meta:
        model=BuildingClearance
        exclude = ['resident_number']

class ConstituentIDSerializer(ModelSerializer):
    
    class Meta:
        model=ConstituentID
        exclude = ['resident_number']

class ResidencySerializer(ModelSerializer):

    class Meta:
        model=Residency
        exclude = ['resident_number']

class BarangayClearanceSerializer(ModelSerializer):

    class Meta:
        model=BarangayClearance
        exclude = ['resident_number']

class ComelecSerializer(ModelSerializer):

    class Meta:
        model=Comelec
        exclude = ['resident_number']


class BusinessClosureSerializer(ModelSerializer):

    class Meta:
        model=BusinessClosure
        exclude = ['resident_number']

class BailBondSerializer(ModelSerializer):

    class Meta:
        model=BailBond
        exclude = ['resident_number']

class GuardianshipSerializer(ModelSerializer):

    class Meta:
        model=Guardianship
        exclude = ['resident_number']
        

class IndigencyBurialSerializer(ModelSerializer):

    class Meta:
        model=IndigencyBurial
        exclude = ['resident_number']

class IndigencyClearanceSerializer(ModelSerializer):

    class Meta:
        model=IndigencyClearance
        exclude = ['resident_number']

class VoucherSerializer(ModelSerializer):

    class Meta:
        model=Voucher
        exclude = ['resident_number']


class BusinessClearanceSerializer(ModelSerializer):

    class Meta:
        model=BusinessClearance
        exclude = ['resident_number']

class ImmunizationSerializer(ModelSerializer):

    class Meta:
        model=Immunization
        exclude = ['resident_number']

class DentalServiceSerializer(ModelSerializer):

    class Meta:
        model=DentalService
        exclude = ['resident_number']

class MaternalCareSerializer(ModelSerializer):

    class Meta:
        model=MaternalCare
        exclude = ['resident_number']

























