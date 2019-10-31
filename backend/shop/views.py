from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import ShopSerializer      # add this
from .models import Shop                     # add this


class ShopView(viewsets.ModelViewSet):       # add this
    serializer_class = ShopSerializer          # add this
    queryset = Shop.objects.all()              # add this
