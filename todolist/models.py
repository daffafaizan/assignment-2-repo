from django.db import models
from django.contrib.auth.models import User

class Todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
