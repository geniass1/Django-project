from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length = 50)
    task = models.TextField('About')

