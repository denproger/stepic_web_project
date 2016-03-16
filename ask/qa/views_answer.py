#!/usr/bin/python
# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from forms import AnswerForm

@require_POST
def add_answer(request):
    form = AnswerForm(request.POST)
    url = '/'
    if form.is_valid():
        answer = form.save()
        question = answer.question
        url = question.get_absolute_url()
    return HttpResponseRedirect(url)