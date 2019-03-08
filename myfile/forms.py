from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import UploadFile

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('title', 'description', 'file')
        widgets = {
            'title': TextInput(attrs={"class":"form-control","placeholder":"Your full name"}),
            'description': TextInput(attrs={"class":"form-control","placeholder":"Your full name"})
        }
