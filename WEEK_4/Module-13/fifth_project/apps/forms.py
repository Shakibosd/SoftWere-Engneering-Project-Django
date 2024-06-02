
from typing import Any
from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Total Length Must Be With In 30 Characters', required=False, widget=forms.Textarea(attrs={'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter Your Full Name'}))
    email = forms.EmailField(label='User Email', initial='@ must')
    file = forms.FileField()
    # age = forms.IntegerField()
    # weight = forms.FloatField(disabled=True)
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    chack = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICEES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large ')]
    size = forms.ChoiceField(choices=CHOICEES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)  
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter With At List 10 Characters')
    
#         if '.com' not in valemail:
#             raise forms.ValidationError('Your Email Must Contain .com   ')
#         return valemail       


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter A Value At List 10 Characters")

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter With At List Minimum 10 Characters')])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter Valid Email')]) 
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message='Age Must Be Mixmum 34'),validators.MinValueValidator(24, message='Age Must Be At List 4')])     
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','jpg'])])
    
    
class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)    
    confiram_password = forms.CharField(widget=forms.PasswordInput)  
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_compass = self.cleaned_data['confiram_password']
        val_name = self.cleaned_data['name']
        if val_compass != val_pass:
            raise forms.ValidationError("Password don't match")
        if len(val_name) < 15:
            raise forms.ValidationError('Name must be at least 15 characters') 