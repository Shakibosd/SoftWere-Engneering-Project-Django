
from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Total Length Must Be With In 30 Characters', required=False, widget=forms.Textarea(attrs={'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter Your Full Name'}))
    email = forms.EmailField(label='User Email', initial='@ must')
    file = forms.FileField()
    age = forms.IntegerField()
    weight = forms.FloatField(disabled=True)
    balance = forms.DecimalField()
    chack = forms.BooleanField()
    birthday = forms.DateField()
    appointment = forms.DateTimeField()
    CHOICEES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large ')]
    size = forms.ChoiceField(choices=CHOICEES)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL)