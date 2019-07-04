from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Community
from django.contrib.auth.decorators import login_required
from . forms import CommunityForm
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
