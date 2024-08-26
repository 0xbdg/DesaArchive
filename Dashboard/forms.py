from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .models import *

'''
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['category','file']
'''
class SuratKeteranganForm(forms.ModelForm):
    class Meta:
        model = SuratKeterangan
        fields = ['file']

class SuratMasukForm(forms.ModelForm):
    class Meta:
        model = SuratMasuk
        fields = ['file']

class SuratKeluarForm(forms.ModelForm):
    class Meta:
        model = SuratKeluar
        fields = ['file']

class AsetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['file']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class SuperuserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(SuperuserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
    
class SuperuserUpdateForm(UserChangeForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label='New Password')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm Password')
    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")