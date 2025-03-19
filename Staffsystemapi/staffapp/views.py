from django.shortcuts import render
from rest_framework import viewsets
from staffapp.models import Item
from staffapp.serializers import ItemSerializers
# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers