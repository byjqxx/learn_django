# -*- encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms

# Create your views here.
def index(request):
    urls = ['login/']
    context = {'urls': urls}
    return render(request, 'form_test/index.html', context)

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            return HttpResponse('Alright', login_form.username)
        else:
            return HttpResponse('Wrong')
    else:
        login_form = forms.LoginForm()
        context = {'loginform': login_form}
        return render(request, 'form_test/login.html', context)