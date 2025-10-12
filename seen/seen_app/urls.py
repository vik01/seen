from django.urls import path
from . import views # Importing views from the current package (file named views.py)

urlpatterns = [
    path('', views.seen, name='seen_app'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),   
    path('communities/', views.communities, name='communities'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_project/add_manual_project/', views.manual_project, name='add_manual_project'),
    path('add_project/connecting_project/', views.connect_waiting, name='connecting_project'),
    path('update_profile/', views.update_profile, name='update_profile'),
]