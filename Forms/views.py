import email
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *
from .mailer import Mailer

from UsersApp.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated

#notification
def email_notification(request):
    MAIL = request.user.email
    Mailer().send(MAIL)

#Cedula
class CedulaList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)
    

class CedulaView(RetrieveUpdateDestroyAPIView):

    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()
    
#BuildingClearance
class BuildingClearanceList(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)
    
class BuildingClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()
   

#ConstituentID
class ConstituentIDList(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class ConstituentIDView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()  

    
#Residency
class ResidencyList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class ResidencyView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all() 

#BarangayClearance

class BarangayClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class BarangayClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all() 

#Comelec

class ComelecList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class ComelecView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all() 

#BusinessClosure

class BusinessClosureList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class BusinessClosureView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all() 

#BailBond

class BailBondList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class BailBondView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()

#Guardianship

class GuardianshipList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class GuardianshipView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

#IndigencyBurial

class IndigencyBurialList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class IndigencyBurialView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

#IndigencyClearance

class IndigencyClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class IndigencyClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

#Voucher

class VoucherList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class VoucherView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

#BusinessClearance

class BusinessClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class BusinessClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

#Immunization

class ImmunizationList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class ImmunizationView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

#DentalService

class DentalServiceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class DentalServiceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()


#MaternalCare

class MaternalCareList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()

    def post(self, request, *args, **kwargs):
        email_notification(request)
        return self.create(request, *args, **kwargs)

class MaternalCareView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()
