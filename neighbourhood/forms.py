from django import forms 
from .models import Community,Post,Profile
class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        exclude = ['name']
class PostsForm(forms.ModelForm):
    class Meta:
        model = Post 
        exclude = ['']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['']        