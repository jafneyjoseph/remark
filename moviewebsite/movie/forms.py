from django import forms
from .models import Profile
from .models import Movie,Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','desc','year','actors','img','youtube_link','category']




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


