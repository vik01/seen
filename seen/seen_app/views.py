from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def seen(request):
    template = loader.get_template('seen_login_page.html')    
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('seen_home_feed.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('seen_profile_page.html')
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