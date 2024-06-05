from django import forms
from django.core import validators
from typing import Any

class contactForm(forms.Form):
      name = forms.CharField(max_length=200,label='User Name', help_text='Total Length Must Be With In 30 Characters', required=True, widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Full Name'}))

      birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))

      comment = forms.CharField(max_length=200,label='Comment', required=True, widget=forms.Textarea(attrs={'placeholder' : 'Enter Your Comment'}))

      email = forms.EmailField(required=True)   

      agree = forms.BooleanField(required=True)

      date = forms.DateField(required=True)

      color = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
      ]
      checkBox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=color, required=True)
 
      age = forms.IntegerField(widget=forms.NumberInput ,required=True)

      file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','jpg'])])

      weight = forms.FloatField(required=True)

      balance = forms.DecimalField()

      appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))

      CHOICEES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large ')]
      size = forms.ChoiceField(choices=CHOICEES, widget=forms.RadioSelect)

      MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]

      pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


      password = forms.CharField(widget=forms.PasswordInput)    
      confiram_password = forms.CharField(widget=forms.PasswordInput)  
    
      def clean(self):
            cleaned_data = super().clean()
            val_pass = cleaned_data.get('password')
            val_compass = cleaned_data.get('confirm_password')
            val_name = cleaned_data.get('name')
            
            if val_pass and val_compass and val_compass != val_pass:
                raise forms.ValidationError("Passwords don't match")
            
            if val_name and len(val_name) < 15:
                raise forms.ValidationError('Name must be at least 15 characters')
