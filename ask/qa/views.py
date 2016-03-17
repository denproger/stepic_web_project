#!/usr/bin/python
# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from views_question import *
from forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def authenticate_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True, u''
        else:
            return False, u'Аккаунт отключен'
    else:
        return False, u'Логин или/и пароль не верны'

def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            isSuccess, error = authenticate_user(request, form.m_username, form.m_password)
            if isSuccess:
                url = '/'
                return HttpResponseRedirect(url)
            else:
                form.add_form_error(error)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form })

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.getData()
            isSuccess, error = authenticate_user(request, username, password)
            if isSuccess:
                url = '/'
                return HttpResponseRedirect(url)
            else:
                form.add_form_error(error)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form })

def logout_user(request):
    logout(request)
    url = '/'
    return HttpResponseRedirect(url)