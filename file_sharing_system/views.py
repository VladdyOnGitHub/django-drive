from django.shortcuts import render, get_object_or_404
from .models import Drive, Directory, File
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RenameForm, EditFileForm


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
    subdirectories = directory.directory_set.all()
    files = directory.file_set.all()

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
    # You can read the file's content here if you have stored it,
    # and then pass it to the template as 'file_content'

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
