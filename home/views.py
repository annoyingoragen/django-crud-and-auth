from re import template
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class HomeView (TemplateView):
    template_name= 'home/welcome.html'
    extra_context= {'today':datetime.today()}

# def home(request):
#     return render (request,'home/welcome.html',{'today':datetime.today()})

class AuthorizedView (LoginRequiredMixin,TemplateView):
    template_name='home/authorized.html'
    login_url='/admin'

# @login_required
# def authorized(request):
#     return render (request,'home/authorized.html',{'today':datetime.today()})

class LoginInterfaceView(LoginView):
     template_name='home/login.html'


class LogoutInterfaceView(LogoutView):
     template_name='home/logout.html'