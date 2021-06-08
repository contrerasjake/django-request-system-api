from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
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
class CedulaSerializer(ModelSerializer):

    class Meta:
        model=Cedula

        fields=['id',
                'resident_number',
                'request_number',
                'birth_place', 
                'profession', 
                'monthly_income', 
                'is_paid', 
                'approval']
                
class BuildingClearanceSerializer(ModelSerializer):

    class Meta:
        model=BuildingClearance

        fields=['id',
                'resident_number',
                'request_number',
                'maintenance_type', 
                'approval']

class ConstituentIDSerializer(ModelSerializer):
    
    class Meta:
        model=ConstituentID

        fields=['id',
                'resident_number',
                'request_number',
                'id_number', 
                'date_received', 
                'signature', 
                'picture',
                'is_paid', 
                'approval']

class ResidencySerializer(ModelSerializer):

    class Meta:
        model=Residency

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'approval']

class BarangayClearanceSerializer(ModelSerializer):

    class Meta:
        model=BarangayClearance

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'has_payment',
                 'is_paid',
                 'approval']

class ComelecSerializer(ModelSerializer):

    class Meta:
        model=Comelec

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'approval']


class BusinessClosureSerializer(ModelSerializer):

    class Meta:
        model=BusinessClosure

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'business_name',
                 'business_owner',
                 'business_address',
                 'business_nature',
                 'approval']

class BailBondSerializer(ModelSerializer):

    class Meta:
        model=BailBond

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'case_number',
                 'is_paid',
                 'approval']

class GuardianshipSerializer(ModelSerializer):

    class Meta:
        model=Guardianship

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'guardian_name'
                 'approval']

class IndigencyBurialSerializer(ModelSerializer):

    class Meta:
        model=IndigencyBurial

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'deceased_relationship',
                 'deceased_name',
                 'passed_onto_whom',
                 'approval']

class IndigencyClearanceSerializer(ModelSerializer):

    class Meta:
        model=IndigencyClearance

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'patient_relationship',
                 'patient_name',
                 'purpose',
                 'passed_onto_whom',
                 'approval']

class VoucherSerializer(ModelSerializer):

    class Meta:
        model=Voucher

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'student_name',
                 'parent_name',
                 'school',
                 'grade',
                 'approval']


class BusinessClearanceSerializer(ModelSerializer):

    class Meta:
        model=BusinessClearance

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'business_name',
                 'business_owner',
                 'business_address',
                 'business_nature',
                 'start_business_operated',
                 'approval']

class ImmunizationSerializer(ModelSerializer):

    class Meta:
        model=Immunization

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'mother_name',
                 'father_name',
                 'birth_height',
                 'birth_height',
                 'approval']

class DentalServiceSerializer(ModelSerializer):

    class Meta:
        model=DentalService

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'approval']

class MaternalCareSerializer(ModelSerializer):

    class Meta:
        model=MaternalCare

        fields= ['id',
                 'resident_number',
                 'request_number',
                 'child_name',
                 'date_of_birth',
                 'birth_place',
                 'approval']

























