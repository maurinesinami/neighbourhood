from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request,'index.html')
def new_community(request):
        