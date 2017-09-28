# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Breed(models.Model):
    """This class represents the dog model."""
    SIZE_CHOICES = (
    ('T', 'Tiny'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ) 
    
    name = models.CharField(max_length=255, blank=False, unique=True)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name) 

class Dog(models.Model):
    """This class represents the dog model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    age = models.IntegerField()
    # breed = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, related_name='DogBreed')
    gender = models.CharField(max_length=1)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=50)
    favoritetoy = models.CharField(max_length=50)
    
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name) 

