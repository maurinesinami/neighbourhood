from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Community,Post,Profile,Business
from django.contrib.auth.decorators import login_required
from . forms import CommunityForm,PostForm,ProfileForm,BusinessForm
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
def new_post(request,id):    
    current_user = request.user
    user_community = Community.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=current_user
            post.neighbourhood = user_community
            post.save()
        return redirect('post',id)

    else:
        form = PostForm()
    return render(request, 'posts/new-post.html', {"form": form,'community':user_community})
    
def post(request,id):
    posts = Post.objects.filter(neighbourhood=id)
    community=Community.objects.get(id=id)
    business = Business.objects.filter(bn_community=id)
    
    return render(request,'posts/post.html',{"posts":posts,"business":business,'community':community})

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
    return render(request, 'posts/new-profile.html', {"form":form,"user":user})
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    
    return render(request, 'posts/profile-page.html',{"profile":profile})
def new_business(request,id):
    user = request.user
    
    user_community = Community.objects.get(id=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = user
            business.bn_community = user_community
            business.save()
        return redirect('business')
    else:
        form = BusinessForm()
    return render(request, 'posts/new-business.html', {"form":form,"user":user,'community':user_community})
def business(request):
    business = Business.objects.all()
    return render(request,'posts/business.html',{"business":business})    
def search_results(request):

    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def leave_hood(request):
    user = Profile.objects.get(user=request.user)
    user.delete()
   
    return redirect('welcome')        