from django import forms
from Manager.models import LibraryPath

class LibraryPathForm(forms.ModelForm):
    class Meta(object):
        model = LibraryPath
        fields = ['type', 'path']