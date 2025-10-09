from django.urls import path
from . import views # Importing views from the current package (file named views.py)

urlpatterns = [
    path('', views.seen, name='seen_app'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),   
    path('communities/', views.communities, name='communities'),
    path('publish_project/', views.publish_project, name='publish_project'),
]