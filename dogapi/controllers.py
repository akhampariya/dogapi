# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#dogapi/controllers.py

from rest_framework import generics
from .serializers import DogSerializer, BreedSerializer
from .models import Dog, Breed

#dog
class DogList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new dog."""
        serializer.save()

class DogDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dog.objects.all()
    serializer_class = DogSerializer

#Breed 

class BreedList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Breed."""
        serializer.save()

class BreedDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer