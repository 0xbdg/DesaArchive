from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'txtbox-username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'txtbox-password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class SuperuserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(SuperuserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user