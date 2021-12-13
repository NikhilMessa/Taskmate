from django.urls import path
from user_app import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),

]

