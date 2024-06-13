from ipo import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IPOInfoViewSet, upcoming_ipo

router = DefaultRouter()
router.register(r'ipo_info', IPOInfoViewSet, basename='ipo_info')

urlpatterns = [
    path('', include(router.urls)),
    path('ipo/', IPOInfoViewSet.as_view({'get': 'list'}), name='ipo'),  
    path('upcoming/', upcoming_ipo, name='upcoming'),
]
