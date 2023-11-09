from django import forms


class RenameForm(forms.Form):
    new_name = forms.CharField(max_length=255)


class EditFileForm(forms.Form):
    new_name = forms.CharField(max_length=255, required=False)
    new_content = forms.CharField(widget=forms.Textarea, required=False)
