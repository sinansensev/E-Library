from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from movies.models import Review, Rating

"""class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']"""
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    