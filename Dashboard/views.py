from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import login, logout
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

class SuperuserManagerView(LoginRequiredMixin,View):
    template_name = "pages/usermanager.html"
    form_class = SuperuserCreationForm

    def get(self, request):
        form = self.form_class()
        user = User.objects.all()
        return render(request, self.template_name, context={'form':form, 'users':user})
    
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('accountmanager')

        return render(request, self.template_name, context={'form':form})

# Action

@login_required
def file_delete(request, id):
    file = Document.objects.get(id=id)
    file.delete()
    os.remove(settings.MEDIA_ROOT / file.file.name)
    return redirect("filemanager")

@login_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('accountmanager')

@login_required
def user_update(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = SuperuserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1:
                if password1 == password2:
                    user.set_password(password1)
                else:
                    form.add_error('password2', "Passwords do not match.")
                    return render(request, 'pages/userupdate.html', {'form': form, 'user': user})

            user.save()
            return redirect('accountmanager')
    else:
        form = SuperuserUpdateForm(instance=user)

    return render(request, 'pages/userupdate.html', {'form': form, 'user': user})

@login_required
def user_logout(request):
    logout(request)
    return redirect("signin")
