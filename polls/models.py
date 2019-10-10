from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="问题")
    publish_date = models.DateTimeField("publish_date", editable=False, default=timezone.now())

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100, verbose_name="选项")
    vote = models.IntegerField(default=0, verbose_name="得票数")

    def __str__(self):
        return self.choice_text
