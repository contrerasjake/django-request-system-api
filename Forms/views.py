from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from .mailer import Mailer

#notification
@api_view(['GET'])
def email_notification(request):
    if request.method == 'GET':    
        MAIL = request.user.email
        Mailer().send(MAIL)
        return HttpResponse ('email success', status=200)

#Cedula
class CedulaList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()


class CedulaView(RetrieveUpdateDestroyAPIView):

    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()
    
#BuildingClearance
class BuildingClearanceList(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()

    
class BuildingClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()
   

#ConstituentID
class ConstituentIDList(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()


class ConstituentIDView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()  

    
#Residency
class ResidencyList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all()


class ResidencyView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all() 

#BarangayClearance

class BarangayClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all()


class BarangayClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all() 

#Comelec

class ComelecList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all()


class ComelecView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all() 

#BusinessClosure

class BusinessClosureList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all()


class BusinessClosureView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all() 

#BailBond

class BailBondList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()


class BailBondView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()

#Guardianship

class GuardianshipList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()


class GuardianshipView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

#IndigencyBurial

class IndigencyBurialList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()


class IndigencyBurialView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

#IndigencyClearance

class IndigencyClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()


class IndigencyClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

#Voucher

class VoucherList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()


class VoucherView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

#BusinessClearance

class BusinessClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()


class BusinessClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

#Immunization

class ImmunizationList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()


class ImmunizationView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

#DentalService

class DentalServiceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()


class DentalServiceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()


#MaternalCare

class MaternalCareList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()


class MaternalCareView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()

