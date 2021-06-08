from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
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
class CedulaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cedula
        fields=('__all__')
                
class BuildingClearanceSerializer(ModelSerializer):

    class Meta:
        model=BuildingClearance
        fields=('__all__')

class ConstituentIDSerializer(ModelSerializer):
    
    class Meta:
        model=ConstituentID
        fields=('__all__')

class ResidencySerializer(ModelSerializer):

    class Meta:
        model=Residency
        fields=('__all__')

class BarangayClearanceSerializer(ModelSerializer):

    class Meta:
        model=BarangayClearance
        fields=('__all__')

class ComelecSerializer(ModelSerializer):

    class Meta:
        model=Comelec
        
        fields=('__all__')


class BusinessClosureSerializer(ModelSerializer):

    class Meta:
        model=BusinessClosure

        fields=('__all__')

class BailBondSerializer(ModelSerializer):

    class Meta:
        model=BailBond

        fields=('__all__')

class GuardianshipSerializer(ModelSerializer):

    class Meta:
        model=Guardianship

        fields=('__all__')
        

class IndigencyBurialSerializer(ModelSerializer):

    class Meta:
        model=IndigencyBurial

        fields=('__all__')

class IndigencyClearanceSerializer(ModelSerializer):

    class Meta:
        model=IndigencyClearance

        fields=('__all__')

class VoucherSerializer(ModelSerializer):

    class Meta:
        model=Voucher

        fields=('__all__')


class BusinessClearanceSerializer(ModelSerializer):

    class Meta:
        model=BusinessClearance

        fields=('__all__')

class ImmunizationSerializer(ModelSerializer):

    class Meta:
        model=Immunization

        fields=('__all__')

class DentalServiceSerializer(ModelSerializer):

    class Meta:
        model=DentalService

        fields=('__all__')

class MaternalCareSerializer(ModelSerializer):

    class Meta:
        model=MaternalCare

        fields=('__all__')

























