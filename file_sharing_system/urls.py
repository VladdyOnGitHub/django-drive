from django.urls import path
from . import views

urlpatterns = [
    path('', views.drive_list, name='drive_list'),
    path('drive/<drive_id>/', views.drive_content, name='drive_content'),
    path('directory/<directory_id>/', views.directory_content, name='directory_content'),
    path('file/<file_id>/', views.file_content, name='file_content'),
    path('login/', views.custom_login, name='custom_login'),
    path('edit_file/<file_id>/', views.edit_file, name='edit_file'),
    path('api/drives/', views.DriveList.as_view(), name='drive-list'),
    path('api/drives/<uuid:pk>/', views.DriveContent.as_view(), name='drive-content'),
    path('api/directories/<uuid:pk>/', views.DirectoryContent.as_view(), name='directory-content'),
    path('api/files/<uuid:pk>/', views.FileContent.as_view(), name='file-content'),
    path('add_directory/<uuid:drive_id>/', views.add_directory, name='add_directory'),
    path('add_file/<uuid:drive_id>/<uuid:directory_id>/', views.add_file, name='add_file'),
    path('delete_directory/<uuid:pk>/', views.delete_directory, name='delete_directory'),
    path('delete_file/<uuid:file_id>/', views.delete_file, name='delete_file'),
    path('edit_drive/<uuid:drive_id>/', views.edit_drive, name='edit-drive'),
    path('edit_directory/<uuid:drive_id>/<uuid:directory_id>/', views.edit_directory, name='edit-directory'),
]

