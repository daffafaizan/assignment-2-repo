from django.forms import ModelForm
from .models import Todolist

class CreateTaskForm(ModelForm):
    class Meta:
        model = Todolist
        fields = ['title', 'description']