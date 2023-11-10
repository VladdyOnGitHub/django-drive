from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RenameForm, EditFileForm, AddDirectoryForm, AddFileForm, DeleteDirectoryForm, DeleteFileForm
from .models import Drive, Directory, File
from rest_framework import generics
from .serializers import DriveSerializer, DirectorySerializer, FileSerializer
from django.urls import reverse


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('drive_list')  # Redirect to the desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'file_sharing_system/login.html', {'form': form})


User = get_user_model()  # Get the user model


@login_required
def drive_list(request):
    if request.user.is_superuser:
        drives = Drive.objects.all()
    else:
        drives = Drive.objects.filter(owner=request.user)

    return render(request, 'file_sharing_system/drive_list.html', {
        'drives': drives,
        'user': request.user
    })


@login_required
def drive_content(request, drive_id):
    # Retrieve the selected drive
    drive = Drive.objects.get(id=drive_id)

    # Retrieve directories and files within the drive
    directories = Directory.objects.filter(drive=drive)
    files = File.objects.filter(drive=drive)

    return render(request, 'file_sharing_system/drive_content.html', {
        'drive_id': drive_id,
        'drive': drive,
        'directories': directories,
        'files': files,
    })


@login_required
def directory_content(request, directory_id):
    # Retrieve the directory
    directory = Directory.objects.get(id=directory_id)

    # Retrieve its subdirectories and files
    subdirectories = directory.subdirectories.all()
    files = directory.files.all()

    return render(request, 'file_sharing_system/directory_content.html', {
        'directory_id': directory_id,
        'directory': directory,
        'subdirectories': subdirectories,
        'files': files,
    })


@login_required
def file_content(request, file_id):
    # Retrieve the file
    file = File.objects.get(id=file_id)

    parent_directory = file.directory if file.directory else file.drive
    # read the file's content here if stored
    # then pass to the template as 'file_content'

    return render(request, 'file_sharing_system/file_content.html', {
        'file_id': file_id,
        'file': file,
        'parent_directory_id': parent_directory.id
    })


@login_required
def rename_drive(request, drive_id):
    drive = get_object_or_404(Drive, id=drive_id)
    if request.method == 'POST':
        form = RenameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']
            drive.rename(new_name)
    else:
        form = RenameForm(initial={'new_name': drive.name})

    return render(request, 'file_sharing_system/rename_drive.html', {
        'form': form,
        'drive': drive
    })


@login_required
def rename_directory(request, directory_id):
    directory = get_object_or_404(Directory, id=directory_id)
    if request.method == 'POST':
        form = RenameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']
            directory.rename(new_name)
    else:
        form = RenameForm(initial={'new_name': directory.name})

    return render(request, 'file_sharing_system/rename_directory.html', {
        'form': form,
        'directory': directory
    })


@login_required
def edit_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    if request.method == 'POST':
        form = EditFileForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']
            new_content = form.cleaned_data['new_content']
            file.edit_content(new_content)

            if new_name:
                file.rename(new_name)
            elif new_content:
                file.edit_content(new_content)

    else:
        form = EditFileForm(initial={'new_name': file.name, 'new_content': file.content})

    return render(request, 'file_sharing_system/edit_file.html', {
        'form': form,
        'file': file
    })


class DriveList(generics.ListCreateAPIView):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer


class DriveContent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer


class DirectoryContent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class FileContent(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


@login_required
def add_directory(request, drive_id):
    drive = get_object_or_404(Drive, id=drive_id)
    if request.method == 'POST':
        form = AddDirectoryForm(request.POST)
        if form.is_valid():
            new_directory = drive.add_directory(form.cleaned_data['name'])
            return redirect(reverse('drive_content', kwargs={'drive_id': drive.id}))
    else:
        form = AddDirectoryForm()

    return render(request, 'file_sharing_system/add_directory.html', {'form': form, 'drive': drive})


@login_required
def add_file(request, drive_id, directory_id=None):
    drive = get_object_or_404(Drive, id=drive_id)
    directory = get_object_or_404(Directory, id=directory_id) if directory_id else None

    if request.method == 'POST':
        form = AddFileForm(request.POST)
        if form.is_valid():
            new_file = drive.add_file(form.cleaned_data['name'], form.cleaned_data['content'], directory)
            return redirect(reverse('drive_content', kwargs={'drive_id': drive.id}))
    else:
        form = AddFileForm()

    return render(request, 'file_sharing_system/add_file.html', {'form': form, 'drive': drive, 'directory': directory})


@login_required
def delete_directory(request, directory_id):
    directory = get_object_or_404(Directory, id=directory_id)
    drive_id = directory.drive.id

    if request.method == 'POST':
        form = DeleteDirectoryForm(request.POST)
        if form.is_valid():
            directory.delete()
            return redirect('drive_content', drive_id=drive_id)
    else:
        form = DeleteDirectoryForm()

    return render(request, 'file_sharing_system/delete_directory.html', {'form': form, 'drive_id': drive_id})


@login_required
def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    drive_id = file.drive.id

    if request.method == 'POST':
        form = DeleteFileForm(request.POST)
        if form.is_valid():
            file.delete()
            return redirect('drive_content', drive_id=drive_id)
    else:
        form = DeleteFileForm()

    return render(request, 'file_sharing_system/delete_file.html', {'form': form, 'drive_id': drive_id})
