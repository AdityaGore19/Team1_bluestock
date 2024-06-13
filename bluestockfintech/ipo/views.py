# ipo/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import IPOInfo
from .serializers import IPOInfoSerializer

def ipo(request):
    return render(request, 'index.html')

def upcomming(request):
    return render(request, 'upcomming.html')

class IPOInfoViewSet(viewsets.ModelViewSet):
    queryset = IPOInfo.objects.all()
    serializer_class = IPOInfoSerializer
    
def upcoming_ipo(request):
    # Logic to get upcoming IPOs
    upcoming_ipos = IPOInfo.objects.filter(status=1)  # Assuming status=1 means upcoming
    return render(request, 'ipo/upcoming.html', {'upcoming_ipos': upcoming_ipos})