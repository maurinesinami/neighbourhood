from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Community,Post,Profile
from django.contrib.auth.decorators import login_required
from . forms import CommunityForm,PostForm,ProfileForm
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def welcome(request):
    communities = Community.objects.all()
    return render(request,'index.html',{"communities":communities})
def new_community(request):
    
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            community = form.save(commit=False)
            community.save()
        return redirect('welcome')

    else:
        form = CommunityForm()
    return render(request, 'new_community.html', {"form": form})
def new_post(request):    
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=current_user
            post.save()
        return redirect('post')

    else:
        form = PostForm()
    return render(request, 'new-post.html', {"form": form})
    
def post(request):
    posts = Post.objects.all()
    return render(request,'post.html',{"posts":posts})
@login_required(login_url='/accounts/login/')      
def new_profile(request,id):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'new-profile.html', {"form":form,"user":user})
    def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    
    return render(request, 'profile-page.html',{"profile":profile})
