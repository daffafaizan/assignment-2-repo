from curses.ascii import CR
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Todolist
from todolist.forms import CreateTaskForm
from django.contrib.auth.models import User

@login_required(login_url='/todolist/login/')
def front_page(request):
    list_todo = Todolist.objects.filter(user=request.user)
    context = {
        'last_login': request.COOKIES['last_login'],
        'username': request.user.username,
        'list_todo': list_todo
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:front_page")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            save = form.save(commit=False)
            save.user = User.objects.get(username=request.user.username)
            save.save()
            return redirect('/todolist/')

    context = {
        'form': form
    }
    return render(request, 'create-task.html', context)

def delete_task(request, pk):
    Todolist.objects.get(user=request.user,pk=pk).delete()
    return HttpResponseRedirect(reverse('todolist:front_page'))