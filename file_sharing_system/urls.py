from django.urls import path
from . import views

urlpatterns = [
    path('', views.drive_list, name='drive_list'),
    path('drive/<int:drive_id>/', views.drive_content, name='drive_content'),
    path('directory/<int:directory_id>/', views.directory_content, name='directory_content'),
    path('file/<int:file_id>/', views.file_content, name='file_content'),
    path('login/', views.custom_login, name='custom_login'),
]
