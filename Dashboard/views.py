from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


import os
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
            user = form.get_user()
            login(request,user)
            return redirect("filemanager")
        
        return render(request, self.template_name, context={'form':form})

class FilemanagerView(LoginRequiredMixin,View):
    template_name = "pages/filemanager.html"
    form_class = DocumentForm

    def get(self, request): 
        docs = Document.objects.all()
        form = self.form_class()
        return render(request, self.template_name, context={'documents':docs, "form":form})
    
    def post(self, request): 
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("filemanager")
        
        return render(request, self.template_name, context={'form':form})

class AccountManagerView(LoginRequiredMixin,View):
    template_name = "pages/accounts.html"
    form_class = SuperuserCreationForm

    def get(self, request):
        form = self.form_class()
        user = User.objects.all()
        return render(request, self.template_name, context={'form':form, 'users':user})
    
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('filemanager')

        return render(request, self.template_name, context={'form':form})

# Action

@login_required
def delete(request, id):
    file = Document.objects.get(id=id)
    file.delete()
    os.remove(settings.MEDIA_ROOT / file.file.name)
    return redirect("filemanager")
