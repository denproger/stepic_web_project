#!/usr/bin/python
# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from views_question import *

def test(request, *args, **kwargs):
    return HttpResponse('OK')


