
from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        modal = TaskModel
        fields = '__all__'      