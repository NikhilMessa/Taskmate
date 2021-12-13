from todolist_app import views 
from django.urls import path

urlpatterns = [
   path('', views.todolist, name='todolist'),
   path('delete/<task_id>', views.delete_task, name='delete_task'),
   path('edit/<task_id>', views.edit_task, name='edit_task'),
   path('complete/<task_id>', views.complete_task, name='complete_task'),
   path('pending/<task_id>', views.pending_task, name='pending_task'),
   path('contact', views.contact, name='contact'),
   path('about-us', views.about, name = 'about')
]