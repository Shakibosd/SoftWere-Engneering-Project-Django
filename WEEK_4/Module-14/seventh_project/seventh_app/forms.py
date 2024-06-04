
from django import forms
from seventh_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll',
        }
        widgets = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write Your Full Name",
        }
        error_messages = {
            'name' : {'required' : 'Your Name Is Requird'},
        }