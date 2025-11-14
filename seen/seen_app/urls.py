from django.contrib import admin
from django.urls import path
from . import views # Importing views from the current package (file named views.py)
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    # Admin paths
    path("admin/", admin.site.urls),

    # Login / logout / signup
    path("accounts/login/",  LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.signup, name="signup"),

    # Password reset flow (optional but recommended)
    path("accounts/password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("accounts/password-reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("accounts/reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # App paths
    path('', views.seen, name='seen_app'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),   
    path('communities/', views.communities, name='communities'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_project/add_manual_project/', views.manual_project, name='add_manual_project'),
    path('add_project/connecting_project/', views.connect_waiting, name='connecting_project'),
    path('update_profile/', views.update_profile, name='update_profile'),
]