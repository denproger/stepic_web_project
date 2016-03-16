#!/usr/bin/python
# coding: utf8
from django.contrib.auth.models import User
from django import forms
from models import Question, Answer

# Форма добавления вопроса
class AskForm(forms.Form):
    title = forms.CharField(label=u'Заголовок вопроса',max_length=255)         # поле заголовка
    text = forms.CharField(label=u'Текст вопроса',widget=forms.Textarea)   # поле текста вопроса

    def clean(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        if title is None or len(title) == 0:
            raise forms.ValidationError(u'Заголовок вопроса не указан')
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Текст вопроса не указан')
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = User.objects.filter()[0]
        question = Question(**self.cleaned_data)
        question.save()
        return question

# Форма добавления ответа
class AnswerForm(forms.Form):
    text = forms.CharField(label=u'Ваш ответ на данный вопрос', widget=forms.Textarea)   # поле текста ответа
    question = forms.IntegerField(widget = forms.HiddenInput()) # поле для связи с вопросом

    def clean(self):
        text = self.cleaned_data.get('text')
        question = self.cleaned_data.get('question')
        print 'text: "{}"'.format(text)
        print 'question: "{}"'.format(question)
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Текст вопроса не указан')
        print 'Question: "{}"'.format(question)
        if question is None or question == 0:
            raise forms.ValidationError(u'Вопрос не выбран')
        try:
            question = Question.objects.get(pk=question)
            self.cleaned_data['question'] = int(question.id)
        except Question.DoesNotExist, ValueError:
            raise forms.ValidationError(u'Выбранного вопроса нет в базе')
        return self.cleaned_data

    def save(self):
        question = Question.objects.get(pk=self.cleaned_data.get('question'))
        author = User.objects.filter()[0]
        answer = Answer(text = self.cleaned_data['text'], question=question, author=author)
        answer.save()
        return answer