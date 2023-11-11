from django import forms
from .models import Drive, Directory, File


class RenameForm(forms.Form):
    new_name = forms.CharField(max_length=255)


class EditFileForm(forms.Form):
    new_name = forms.CharField(max_length=255, required=False)
    new_content = forms.CharField(widget=forms.Textarea, required=False)


class DriveForm(forms.ModelForm):
    class Meta:
        model = Drive
        fields = ['name', 'reader_access', 'public_access']


class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'reader_access', 'public_access']


class AddDirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'reader_access', 'public_access']


class AddFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'content']


class DeleteDirectoryForm(forms.Form):
    directory_id = forms.UUIDField(widget=forms.HiddenInput, required=False)


class DeleteFileForm(forms.Form):
    file_id = forms.UUIDField(widget=forms.HiddenInput, required=False)
