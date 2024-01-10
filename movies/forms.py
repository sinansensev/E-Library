from django import forms 
from django.contrib.auth.models import User
from movies.models import Review, Rating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']


# forms.py
