from django.urls import path
from .views import ListUser

urlpatterns = [
    path('', ListUser.as_view(), name='Users'),
    path('<int:pk>/', ListUser.as_view(), name='SingleUser'),
]