from django.urls import path
from . import views

urlpatterns = [
    path('', views.drive_list, name='drive_list'),
    path('drive/<drive_id>/', views.drive_content, name='drive_content'),
    path('directory/<directory_id>/', views.directory_content, name='directory_content'),
    path('file/<file_id>/', views.file_content, name='file_content'),
    path('login/', views.custom_login, name='custom_login'),
]
