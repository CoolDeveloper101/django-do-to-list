from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    date_started = models.DateTimeField()

    def __str__(self):
        return self.task


class DoneTask(models.Model):
    task = models.CharField(max_length=200)
    date_started = models.DateTimeField()
    date_done = models.DateTimeField()