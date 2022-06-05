from django.http import HttpResponse
from django.shortcuts import render
from UsersApp.serializers import UserSerializer, UserInformationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response
from drf_multiple_model.views import FlatMultipleModelAPIView, ObjectMultipleModelAPIView

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
    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class CedulaView(RetrieveUpdateDestroyAPIView):
    serializer_class = CedulaSerializer
    queryset = Cedula.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = Cedula.objects.get(request_number=request.data["request_number"])
            else:
                form = Cedula.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = CedulaSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Cedula.objects.get(request_number=self.request.data["request_number"])
            else:
                form = Cedula.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Cedula.objects.get(request_number=request.data["request_number"])
            else:
                form = Cedula.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#BuildingClearance
class BuildingClearanceList(ListCreateAPIView):
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class BuildingClearanceView(RetrieveUpdateDestroyAPIView):
    serializer_class = BuildingClearanceSerializer
    queryset = BuildingClearance.objects.all()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = BuildingClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = BuildingClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = BuildingClearanceSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BuildingClearance.objects.get(request_number=self.request.data["request_number"])
            else:
                form = BuildingClearance.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BuildingClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = BuildingClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)
   

#ConstituentID
class ConstituentIDList(ListCreateAPIView):
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class ConstituentIDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ConstituentIDSerializer
    queryset = ConstituentID.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = ConstituentID.objects.get(request_number=request.data["request_number"])
            else:
                form = ConstituentID.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = ConstituentIDSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = ConstituentID.objects.get(request_number=self.request.data["request_number"])
            else:
                form = ConstituentID.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = ConstituentID.objects.get(request_number=request.data["request_number"])
            else:
                form = ConstituentID.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

    
#Residency
class ResidencyList(ListCreateAPIView):
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class ResidencyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ResidencySerializer
    queryset = Residency.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = Residency.objects.get(request_number=request.data["request_number"])
            else:
                form = Residency.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = ResidencySerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Residency.objects.get(request_number=self.request.data["request_number"])
            else:
                form = Residency.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Residency.objects.get(request_number=request.data["request_number"])
            else:
                form = Residency.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#BarangayClearance

class BarangayClearanceList(ListCreateAPIView):
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class BarangayClearanceView(RetrieveUpdateDestroyAPIView):
    serializer_class = BarangayClearanceSerializer
    queryset = BarangayClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = BarangayClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = BarangayClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = BarangayClearanceSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BarangayClearance.objects.get(request_number=self.request.data["request_number"])
            else:
                form = BarangayClearance.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BarangayClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = BarangayClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#Comelec

class ComelecList(ListCreateAPIView):
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class ComelecView(RetrieveUpdateDestroyAPIView):
    serializer_class = ComelecSerializer
    queryset = Comelec.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = Comelec.objects.get(request_number=request.data["request_number"])
            else:
                form = Comelec.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = ComelecSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Comelec.objects.get(request_number=self.request.data["request_number"])
            else:
                form = Comelec.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Comelec.objects.get(request_number=request.data["request_number"])
            else:
                form = Comelec.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#BusinessClosure

class BusinessClosureList(ListCreateAPIView):
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class BusinessClosureView(RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessClosureSerializer
    queryset = BusinessClosure.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = BusinessClosure.objects.get(request_number=request.data["request_number"])
            else:
                form = BusinessClosure.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = BusinessClosureSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BusinessClosure.objects.get(request_number=self.request.data["request_number"])
            else:
                form = BusinessClosure.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BusinessClosure.objects.get(request_number=request.data["request_number"])
            else:
                form = BusinessClosure.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#BailBond

class BailBondList(ListCreateAPIView):
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class BailBondView(RetrieveUpdateDestroyAPIView):
    serializer_class = BailBondSerializer
    queryset = BailBond.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = BailBond.objects.get(request_number=request.data["request_number"])
            else:
                form = BailBond.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = BailBondSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BailBond.objects.get(request_number=self.request.data["request_number"])
            else:
                form = BailBond.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BailBond.objects.get(request_number=request.data["request_number"])
            else:
                form = BailBond.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#Guardianship

class GuardianshipList(ListCreateAPIView):
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class GuardianshipView(RetrieveUpdateDestroyAPIView):
    serializer_class = GuardianshipSerializer
    queryset = Guardianship.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = Guardianship.objects.get(request_number=request.data["request_number"])
            else:
                form = Guardianship.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = GuardianshipSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Guardianship.objects.get(request_number=self.request.data["request_number"])
            else:
                form = Guardianship.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Guardianship.objects.get(request_number=request.data["request_number"])
            else:
                form = Guardianship.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#IndigencyBurial

class IndigencyBurialList(ListCreateAPIView):
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class IndigencyBurialView(RetrieveUpdateDestroyAPIView):
    serializer_class = IndigencyBurialSerializer
    queryset = IndigencyBurial.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = IndigencyBurial.objects.get(request_number=request.data["request_number"])
            else:
                form = IndigencyBurial.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = IndigencyBurialSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = IndigencyBurial.objects.get(request_number=self.request.data["request_number"])
            else:
                form = IndigencyBurial.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = IndigencyBurial.objects.get(request_number=request.data["request_number"])
            else:
                form = IndigencyBurial.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#IndigencyClearance

class IndigencyClearanceList(ListCreateAPIView):
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class IndigencyClearanceView(RetrieveUpdateDestroyAPIView):
    serializer_class = IndigencyClearanceSerializer
    queryset = IndigencyClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = IndigencyClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = IndigencyClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = IndigencyClearanceSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = IndigencyClearance.objects.get(request_number=self.request.data["request_number"])
            else:
                form = IndigencyClearance.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = IndigencyClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = IndigencyClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#Voucher

class VoucherList(ListCreateAPIView):
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class VoucherView(RetrieveUpdateDestroyAPIView):
    serializer_class = VoucherSerializer
    queryset = Voucher.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = Voucher.objects.get(request_number=request.data["request_number"])
            else:
                form = Voucher.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = VoucherSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Voucher.objects.get(request_number=self.request.data["request_number"])
            else:
                form = Voucher.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Voucher.objects.get(request_number=request.data["request_number"])
            else:
                form = Voucher.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#BusinessClearance

class BusinessClearanceList(ListCreateAPIView):
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class BusinessClearanceView(RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessClearanceSerializer
    queryset = BusinessClearance.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = BusinessClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = BusinessClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = BusinessClearanceSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BusinessClearance.objects.get(request_number=self.request.data["request_number"])
            else:
                form = BusinessClearance.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = BusinessClearance.objects.get(request_number=request.data["request_number"])
            else:
                form = BusinessClearance.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#Immunization

class ImmunizationList(ListCreateAPIView):
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class ImmunizationView(RetrieveUpdateDestroyAPIView):
    serializer_class = ImmunizationSerializer
    queryset = Immunization.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = Immunization.objects.get(request_number=request.data["request_number"])
            else:
                form = Immunization.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = ImmunizationSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Immunization.objects.get(request_number=self.request.data["request_number"])
            else:
                form = Immunization.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = Immunization.objects.get(request_number=request.data["request_number"])
            else:
                form = Immunization.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#DentalService

class DentalServiceList(ListCreateAPIView):
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class DentalServiceView(RetrieveUpdateDestroyAPIView):
    serializer_class = DentalServiceSerializer
    queryset = DentalService.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = DentalService.objects.get(request_number=request.data["request_number"])
            else:
                form = DentalService.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = DentalServiceSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = DentalService.objects.get(request_number=self.request.data["request_number"])
            else:
                form = DentalService.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = DentalService.objects.get(request_number=request.data["request_number"])
            else:
                form = DentalService.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#MaternalCare

class MaternalCareList(ListCreateAPIView):
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

class MaternalCareView(RetrieveUpdateDestroyAPIView):
    serializer_class = MaternalCareSerializer
    queryset = MaternalCare.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    def get(self, request):
        user = self.request.user
        try:
            if(user.is_staff):
                form = MaternalCare.objects.get(request_number=request.data["request_number"])
            else:
                form = MaternalCare.objects.get(resident_number=user, request_number=request.data["request_number"])
            serializer = MaternalCareSerializer(form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("request does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            user = self.request.user
            if(user.is_staff):
                form = MaternalCare.objects.get(request_number=self.request.data["request_number"])
            else:
                form = MaternalCare.objects.get(resident_number=user, request_number=self.request.data["request_number"])
            self.check_object_permissions(self.request, form)
            return form
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = self.request.user
            if(user.is_staff):
                form = MaternalCare.objects.get(request_number=request.data["request_number"])
            else:
                form = MaternalCare.objects.get(resident_number=user, request_number=request.data["request_number"])
        except:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)
        form.delete()
        return Response("form deleted", status=status.HTTP_200_OK)

#AllForms for one resident number
class AllFormsView(FlatMultipleModelAPIView):
    permission_classes = [IsAuthenticated]

    def get_querylist(self):
        user = self.request.user
        allCedula = Cedula.objects.filter(resident_number=user)
        allBuildingClearance = BuildingClearance.objects.filter(resident_number=user)
        allConstituentID = ConstituentID.objects.filter(resident_number=user)
        allResidency = Residency.objects.filter(resident_number=user)
        allBarangayClearance = BarangayClearance.objects.filter(resident_number=user)
        allComelec = Comelec.objects.filter(resident_number=user)
        allBusinessClosure = BusinessClosure.objects.filter(resident_number=user)
        allBailBond = BailBond.objects.filter(resident_number=user)
        allGuardianship = Guardianship.objects.filter(resident_number=user)
        allIndigencyBurial = IndigencyBurial.objects.filter(resident_number=user)
        allIndigencyClearance = IndigencyClearance.objects.filter(resident_number=user)
        allVoucher = Voucher.objects.filter(resident_number=user)
        allBusinessClearance = BusinessClearance.objects.filter(resident_number=user)
        allImmunization = Immunization.objects.filter(resident_number=user)
        allDentalService = DentalService.objects.filter(resident_number=user)
        allMaternalCare = MaternalCare.objects.filter(resident_number=user)
        querylist = [
            {'queryset': allCedula, 'serializer_class': CedulaSerializer},
            {'queryset': allBuildingClearance, 'serializer_class': BuildingClearanceSerializer},
            {'queryset': allConstituentID, 'serializer_class': ConstituentIDSerializer},
            {'queryset': allResidency, 'serializer_class': ResidencySerializer},
            {'queryset': allBarangayClearance, 'serializer_class': BarangayClearanceSerializer},
            {'queryset': allComelec, 'serializer_class': ComelecSerializer},
            {'queryset': allBusinessClosure, 'serializer_class': BusinessClosureSerializer},
            {'queryset': allBailBond, 'serializer_class': BailBondSerializer},
            {'queryset': allGuardianship, 'serializer_class': GuardianshipSerializer},
            {'queryset': allIndigencyBurial, 'serializer_class': IndigencyBurialSerializer},
            {'queryset': allIndigencyClearance, 'serializer_class': IndigencyClearanceSerializer},
            {'queryset': allVoucher, 'serializer_class': VoucherSerializer},
            {'queryset': allBusinessClearance, 'serializer_class': BusinessClearanceSerializer},
            {'queryset': allImmunization, 'serializer_class': ImmunizationSerializer},
            {'queryset': allDentalService, 'serializer_class': DentalServiceSerializer},
            {'queryset': allMaternalCare, 'serializer_class': MaternalCareSerializer},
        ]
        return querylist
