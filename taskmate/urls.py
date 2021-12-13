from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('todolist/' ,include('todolist_app.urls')),
    path('account/' ,include('user_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name = 'about')
]

urlpatterns += staticfiles_urlpatterns()