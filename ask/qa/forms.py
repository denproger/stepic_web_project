#!/usr/bin/python
# coding: utf8
from django.contrib.auth.models import User
from django import forms
from models import Question, Answer
from django.forms.util import ErrorDict
from django.forms.forms import NON_FIELD_ERRORS

# Форма добавления вопроса
class AskForm(forms.Form):
    title = forms.CharField(label=u'Заголовок вопроса',max_length=255)         # поле заголовка
    text = forms.CharField(label=u'Текст вопроса',widget=forms.Textarea)   # поле текста вопроса

    def setUser(self, user):
        self._user = user

    def clean(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        if title is None or len(title) == 0:
            raise forms.ValidationError(u'Заголовок вопроса не указан')
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Текст вопроса не указан')
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

# Форма добавления ответа
class AnswerForm(forms.Form):
    text = forms.CharField(label=u'Ваш ответ на данный вопрос', widget=forms.Textarea)   # поле текста ответа
    question = forms.IntegerField(widget = forms.HiddenInput()) # поле для связи с вопросом

    def setUser(self, user):
        self._user = user

    def clean(self):
        self.m_question = 0;

        question = self.cleaned_data.get('question')
        if question is None or question == 0:
            raise forms.ValidationError(u'Вопрос не выбран')
        try:
            question = Question.objects.get(pk=question)
            self.m_question = int(question.id)
            self.cleaned_data['question'] = self.m_question
        except Question.DoesNotExist, ValueError:
            raise forms.ValidationError(u'Выбранного вопроса нет в базе')

        text = self.cleaned_data.get('text')
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Текст вопроса не указан')
        return self.cleaned_data

    def save(self):
        question = Question.objects.get(pk=self.cleaned_data.get('question'))
        answer = Answer(text = self.cleaned_data['text'],
                        question=question,
                        author=self._user)
        answer.save()
        return answer

# Форма регистрации пользователя
class SignupForm(forms.Form):
    username = forms.CharField(label=u'Логин',max_length=255)# имя пользователя, логин
    email = forms.EmailField(label=u'email') # email пользователя
    password = forms.CharField(label=u'Пароль',widget=forms.PasswordInput,max_length=255) # пароль пользователя

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username is None or len(username) == 0:
            raise forms.ValidationError(u'Логин пользователя не указан')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None or len(email) == 0:
            raise forms.ValidationError(u'email пользователя не указан')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is None or len(password) == 0:
            raise forms.ValidationError(u'email пользователя не указан')
        return password

    def save(self):
        self.m_username = self.cleaned_data.get('username')
        self.m_email = self.cleaned_data.get('email')
        self.m_password = self.cleaned_data.get('password')
        user = User.objects.create_user( username=self.m_username,
                                         email=self.m_email,
                                         password=self.m_password )
        user.save()
        return user

    def add_form_error(self, message):
        if not self._errors:
            self._errors = ErrorDict()
        if not NON_FIELD_ERRORS in self._errors:
            self._errors[NON_FIELD_ERRORS] = self.error_class()
        self._errors[NON_FIELD_ERRORS].append(message)

# Форма регистрации пользователя
class LoginForm(forms.Form):
    username = forms.CharField(label=u'Логин',max_length=255)# имя пользователя, логин
    password = forms.CharField(label=u'Пароль',widget=forms.PasswordInput,max_length=255) # пароль пользователя

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username is None or len(username) == 0:
            raise forms.ValidationError(u'Логин пользователя не указан')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is None or len(password) == 0:
            raise forms.ValidationError(u'email пользователя не указан')
        return password

    def getData(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return username, password

    def add_form_error(self, message):
        if not self._errors:
            self._errors = ErrorDict()
        if not NON_FIELD_ERRORS in self._errors:
            self._errors[NON_FIELD_ERRORS] = self.error_class()
        self._errors[NON_FIELD_ERRORS].append(message)