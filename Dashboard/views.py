from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.

class SigninView(View):
    form_class = LoginForm
    template_name = "pages/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and (user.is_superuser or user.is_staff):
                login(request, user)
                redirect('filemanager')
        return render(request, self.template_name, context={'form':form})
    
@login_required
class FilemanagerView(View):
    template_name = "pages/filemanager.html"

    def get(self, request): 
        return render(request, self.template_name, context={})

@login_required
class AccountManagerView(View):
    template_name = "pages/accounts.html"
    form_class = SuperuserCreationForm()

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={})
    
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('')

        return render(request, self.template_name, context={})
