from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=51)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_users = models.ManyToManyField(User)
    files = models.FileField(upload_to='filesi/')

class TaskHistory(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    status_change_date = models.DateTimeField()
    old_status = models.CharField(max_length=53)
    new_status = models.CharField(max_length=55)
    change_by = models.CharField(max_length=54)

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=65)
    parol = models.CharField(max_length=12)