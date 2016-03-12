#!/usr/bin/python
# coding: utf8
from django.db import models
from django.contrib.auth.models import User

# Модель вопроса
class Question(models.Model):
    title = models.CharField(max_length=255)            # заголовок вопроса
    text = models.TextField()                           # полный текст вопроса
    added_at = models.DateTimeField(auto_now_add=True)  # дата добавления вопроса
    rating = models.IntegerField(default=0)             # рейтинг вопроса (число)
    author = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE )# автор вопроса
    likes = models.ManyToManyField(User) # список пользователей, поставивших "лайк"

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        ordering = ['-added_at']

# Модель ответа
class Answer(models.Model):
    text = models.TextField()                           # текст ответа
    added_at = models.DateTimeField(auto_now_add=True)  # дата добавления ответа
    question = models.ForeignKey(Question,on_delete=models.CASCADE)  # вопрос, к которому относится ответ
    author = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE ) # автор ответа

    class Meta:
        ordering = ['-added_at']


