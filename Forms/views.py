from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *

from rest_framework.permissions import AllowAny
from UsersApp.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated


#Cedula
class CedulaList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class CedulaView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)
    
#BuildingClearance
class BuildingClearanceList(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)
    
class BuildingClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)
   

#ConstituentID
class ConstituentIDList(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)
class ConstituentIDView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()  

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#Residency
class ResidencyList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class ResidencyView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all() 

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#BarangayClearance

class BarangayClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class BarangayClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all() 

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#Comelec

class ComelecList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class ComelecView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all() 

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#BusinessClosure

class BusinessClosureList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class BusinessClosureView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all() 

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#BailBond
class BailBondList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BailBond.objects.all()
    serializer_class = BailBondSerializer
    
    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class BailBondView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#Guardianship

class GuardianshipList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class GuardianshipView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#IndigencyBurial

class IndigencyBurialList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class IndigencyBurialView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#IndigencyClearance

class IndigencyClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class IndigencyClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#Voucher

class VoucherList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class VoucherView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#BusinessClearance

class BusinessClearanceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class BusinessClearanceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#Immunization

class ImmunizationList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class ImmunizationView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

#DentalService

class DentalServiceList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class DentalServiceView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)


#MaternalCare

class MaternalCareList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)

class MaternalCareView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()

    def perform_create(self, serializer):
        return serializer.save(resident_number=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(resident_number=self.request.user)





