from django import forms 
from .models import Community,Post,Profile
class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        exclude = ['name']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        exclude = ['profile','neighbourhood']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']        