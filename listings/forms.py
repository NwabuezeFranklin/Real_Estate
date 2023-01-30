from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [  
          'title',
          'price',
          'num_bedrooms',
          'num_bathrooms',
          'square_footage',
          'address',
          'image',
        ]