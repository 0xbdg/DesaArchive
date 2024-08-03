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

class FilemanagerView(View):
    template_name = "pages/filemanager.html"
    form_class = DocumentForm

    def get(self, request): 
        docs = Document.objects.all()
        return render(request, self.template_name, context={'documents':docs})
    
    def post(self, request): 
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("filemanager")
        
        return render(request, self.template_name, context={'form':form})

class AccountManagerView(View):
    template_name = "pages/accounts.html"
    form_class = SuperuserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})
    
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('')

        return render(request, self.template_name, context={'form':form})

# Action

def delete(request, id):
    file = Document.objects.get(id=id)
    file.delete()
    return redirect("filemanager")
