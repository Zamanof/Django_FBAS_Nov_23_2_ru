from django import forms
from unicodedata import category

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','category','description']
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control', "placeholder":"Task name"}),
            "description": forms.TextInput(attrs={'class':'form-control', "placeholder":"Task description"}),
        }