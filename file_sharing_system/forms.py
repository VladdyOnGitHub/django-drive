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
        fields = ['name', 'reader_access', 'public_access', 'parent_directory']

    def __init__(self, current_drive, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter the queryset to include only directories in the current drive
        self.fields['parent_directory'].queryset = Directory.objects.filter(drive=current_drive)
        self.fields['parent_directory'].label_from_instance = lambda obj: obj.name if obj else 'Root Directory'

    def clean_parent_directory(self):
        parent_directory = self.cleaned_data['parent_directory']
        if parent_directory and parent_directory.drive != self.instance.drive:
            raise forms.ValidationError("Selected parent directory is not in the same drive.")
        return parent_directory


class AddFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'content']


class DeleteDirectoryForm(forms.Form):
    directory_id = forms.UUIDField(widget=forms.HiddenInput, required=False)


class DeleteFileForm(forms.Form):
    file_id = forms.UUIDField(widget=forms.HiddenInput, required=False)
