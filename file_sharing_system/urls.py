from django.urls import path
from . import views

urlpatterns = [
    path('', views.drive_list, name='drive_list'),
    path('drive/<drive_id>/', views.drive_content, name='drive_content'),
    path('directory/<directory_id>/', views.directory_content, name='directory_content'),
    path('file/<file_id>/', views.file_content, name='file_content'),
    path('login/', views.custom_login, name='custom_login'),
    path('rename_drive/<drive_id>/', views.rename_drive, name='rename_drive'),
    path('rename_directory/<directory_id>/', views.rename_directory, name='rename_directory'),
    path('edit_file/<file_id>/', views.edit_file, name='edit_file'),
]
