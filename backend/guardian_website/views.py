from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GuardianSerializer
from .models import Guardian

# Create your views here.
class GuardianView(viewsets.ModelViewSet):
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()