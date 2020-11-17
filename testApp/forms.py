from django import forms
from django.core import validators

class Login(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd != inputrpwd:
            raise forms.ValidationError('password not matched')

class logout(forms.Form):
    email=forms.EmailField()
    pwd=forms.CharField(widget=forms.PasswordInput)

class feedback(forms.Form):
    feedback=forms.CharField(widget=forms.Textarea)
