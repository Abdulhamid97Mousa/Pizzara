from django.forms import ModelForm

from .models import ProjectFile
from django import forms
from django.core.validators import FileExtensionValidator


class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['name', 'attachment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].validators = [
            FileExtensionValidator(allowed_extensions=['pdf', 'docx'])
        ]