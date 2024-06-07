
from django import forms
from .models import TaskCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        modal = TaskCategory
        fields = '__all__'              