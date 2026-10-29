from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Women
from .serializers import WomenSerializer
# Create your views here.

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.filter(is_published=True).order_by('id')
    serializer_class = WomenSerializer
    permission_classes = [AllowAny]
    pagination_class = None