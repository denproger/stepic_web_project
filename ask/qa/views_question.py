#!/usr/bin/python
# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Question, Answer
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from forms import AskForm, AnswerForm
from django.contrib.auth.decorators import login_required

def paginate(request, qs, default_limit=10, max_limit=100 ):
    try:
        limit = int(request.GET.get('limit', default_limit))
    except ValueError:
        limit = default_limit
    if limit > max_limit:
        limit = default_limit
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

@require_GET
def get_new_questions(request):
    questions = Question.objects.all().order_by('-added_at')
    paginator, page = paginate( request, questions)
    paginator.baseurl = reverse('main') + '?page='
    return render(request, 'main.html', {
         'questions': page.object_list,
         'paginator': paginator, 'page': page,
    })

@require_GET
def get_popular_questions(request):
    questions = Question.objects.all().order_by('-rating')
    paginator, page = paginate( request, questions)
    paginator.baseurl = reverse('popular') + '?page='
    return render(request, 'popular.html', {
         'questions': page.object_list,
         'paginator': paginator, 'page': page,
    })

@login_required(login_url='/login/')
def question_details(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form.setUser(request.user)
        if form.is_valid():
            answer = form.save()
            question = answer.question
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        default_data = {'question': question.id}
        form = AnswerForm(initial=default_data);
    answers = Answer.objects.filter(question=question).order_by('-added_at')
    return render(request, 'question.html', {
                  'question': question,
                  'answers': answers,
                  'form': form,
    })

@login_required(login_url='/login/')
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form.setUser(request.user)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form })

