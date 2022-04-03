from django.urls import path
from .views import *

urlpatterns = [
    path('cedula/', CedulaList.as_view()),
    path('cedula/<int:pk>/', CedulaView.as_view()),
    path('constituent/', ConstituentIDList.as_view()),
    path('constituent/<int:pk>/', ConstituentIDView.as_view()),
    path('building/', BuildingClearanceList.as_view()),
    path('building/<int:pk>/', BuildingClearanceView.as_view()),
    path('residency/', ResidencyList.as_view()),
    path('residency/<int:pk>/', ResidencyView.as_view()),
    path('barangay-clearance/', BarangayClearanceList.as_view()),
    path('barangay-clearance/<int:pk>/', BarangayClearanceView.as_view()),
    path('comelec/', ComelecList.as_view()),
    path('comelec/<int:pk>/', ComelecView.as_view()),
    path('business-closure/', BusinessClosureList.as_view()),
    path('business-closure/<int:pk>/', BusinessClosureView.as_view()),
    path('bailbond/', BailBondList.as_view()),
    path('bailbond/<int:pk>/', BailBondView.as_view()),
    path('guardianship/', GuardianshipList.as_view()),
    path('guardianship/<int:pk>/', GuardianshipView.as_view()),
    path('indigency-burial/', IndigencyBurialList.as_view()),
    path('indigency-burial/<int:pk>/', IndigencyBurialView.as_view()),
    path('indigency-clearance/', IndigencyClearanceList.as_view()),
    path('indigency-clearance/<int:pk>/', IndigencyClearanceView.as_view()),
    path('voucher/', VoucherList.as_view()),
    path('voucher/<int:pk>/', VoucherView.as_view()),
    path('business-clearance/', BusinessClearanceList.as_view()),
    path('business-clearance/<int:pk>/', BusinessClearanceView.as_view()),
    path('immunization/', ImmunizationList.as_view()),
    path('immunization/<int:pk>/', ImmunizationView.as_view()),
    path('dental-service/', DentalServiceList.as_view()),
    path('dental-service/<int:pk>/', DentalServiceView.as_view()),
    path('maternal-care/', MaternalCareList.as_view()),
    path('maternal-care/<int:pk>/', MaternalCareView.as_view()),



]