#!/usr/bin/python
# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from forms import AnswerForm
from views_question import question_details

@require_POST
def add_answer(request):
    form = AnswerForm(request.POST)
    form.is_valid()
    return question_details(request, form.m_question)