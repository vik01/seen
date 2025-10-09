from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def seen(request):
    template = loader.get_template('seen_login_page.html')    
    return HttpResponse(template.render())

def home(request):
    return render(request, 'seen_home_feed.html')

def profile(request):
    return render(request, 'seen_profile_page.html')

def communities(request):
    return render(request, 'seen_communities_page.html')

def publish_project(request):
    return render(request, 'seen_publish_project.html')