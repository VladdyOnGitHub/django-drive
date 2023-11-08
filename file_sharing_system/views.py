from django.shortcuts import render
from .models import Drive, Directory, File


def drive_list(request):
    # Retrieve all drives
    drives = Drive.objects.all()

    return render(request, 'file_sharing_system/drive_list.html', {
        'drives': drives,
    })


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


def directory_content(request, directory_id):
    # Retrieve the directory
    directory = Directory.objects.get(id=directory_id)

    # Retrieve its subdirectories and files
    subdirectories = directory.directory_set.all()
    files = directory.file_set.all()

    return render(request, 'file_sharing_system/directory_content.html', {
        'directory_id': directory_id,
        'subdirectories': subdirectories,
        'files': files,
    })


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

