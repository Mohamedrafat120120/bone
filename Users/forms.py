from django import forms
from .models import Users_Authrization


class Login_Form(forms.ModelForm):
    class Meta:
        model=Users_Authrization
        fields = '__all__'