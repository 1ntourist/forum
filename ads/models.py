from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class Ads(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads_author')
    title = models.CharField(max_length=255)
    body = models.TextField()
    file = models.FileField(upload_to='images/', default='images/default.png')
    date = models.DateTimeField(default=datetime.now)
    rubric = models.ForeignKey('Rubric', on_delete=False, related_name='ads_rubric', default=None)
    theme = models.ForeignKey('Theme', on_delete=False, related_name='ads_theme')

    def __str__(self):
        return f'{self.author}, {self.title}, {self.date}'


class Rubric(models.Model):
    rubric = models.CharField(max_length=255)

    def __str__(self):
        return self.rubric


class Theme(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE, related_name='rubric_theme')
    theme = models.CharField(max_length=255)

    def __str__(self):
        return self.theme