# -*- encoding:utf-8
from django import contrib
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import sessions

# Create your views here.
def index(request):
    urls = ['user_login', 'user_register']
    context = {'urls': urls}
    return render(request, 'form_test/index.html', context)

def user_login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            # username = request.POST['username']
            # password = request.POST['userpassword']
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['userpassword']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session.set_expiry(60)
                # return HttpResponse('Alright', login_form.cleaned_data['username'])
                # return HttpResponse('Alright, %s' %user.username)
                return HttpResponseRedirect('/form/info')
            else:
                return HttpResponse('%s dose not exist or password error' % login_form.cleaned_data['username'])
        else:
            return HttpResponse('Wrong')
    else:
        login_form = forms.LoginForm()
        context = {'loginform': login_form}
        return render(request, 'form_test/login.html', context)


def user_register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            uname = register_form.cleaned_data['username']
            upasswd = register_form.cleaned_data['userpassword']
            uemail = register_form.cleaned_data['useremail']
            user = User.objects.create_user(username=uname, password=upasswd, email=uemail)
            login(request, user)
            request.session.set_expiry(60)
            return HttpResponseRedirect('/form/info')
        else:
            return HttpResponse('您输入的帐号名或密码不符合要求！')
    else:
        register_form = forms.RegisterForm()
        return render(request, 'form_test/register.html', {'registerform': register_form})

@login_required(login_url='/form/user_login/')
def info(request):
    user1 = request.user
    # userid = request.session['_auth_user_id']
    # user = User.objects.get(id=userid)
    userinfo = { 'username': user1.username, 'useremail': user1.email}
    return render(request, 'form_test/info.html', {'user_info': userinfo})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/form/user_login')