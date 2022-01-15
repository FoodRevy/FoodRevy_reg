from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [

    path('', views.home, name="home"),

    path("signup/", views.signup, name="signup"),
    path("signin/", auth_view.LoginView.as_view(template_name='users/signin.html'), name="signin"),
]
