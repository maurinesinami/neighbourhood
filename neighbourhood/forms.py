from django import forms 
from .models import Community,Post,Profile,Business
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
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['bn_user','bn_community']        