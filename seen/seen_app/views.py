from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after signup
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def seen(request):
    template = loader.get_template('seen_login_page.html')    
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('seen_home_feed.html')
    return HttpResponse(template.render())

@login_required(login_url="login")
def profile(request):
    template = loader.get_template('seen_profile_page.html')
    return HttpResponse(template.render())

def update_profile(request):
    template = loader.get_template('seen_profile_page_stage_2.html')
    return HttpResponse(template.render())

def communities(request):
    template = loader.get_template('seen_communities_page.html')
    return HttpResponse(template.render())

def add_project(request):
    template = loader.get_template('seen_add_project.html')
    return HttpResponse(template.render())

def manual_project(request):
    template = loader.get_template('seen_publish_project.html')
    return HttpResponse(template.render())

def connect_waiting(request):
    template = loader.get_template('connecting_project.html')
    return HttpResponse(template.render())

    # platform = request.GET.get('platform', '')
    # return render(request, 'connecting_project.html', {'platform': platform})