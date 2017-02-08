from django import forms
from fruitclub.models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name', 'picture')
