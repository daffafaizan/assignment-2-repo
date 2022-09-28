from django.urls import path
from todolist.views import front_page, register, login_user, logout_user, create_task

app_name = 'todolist'

urlpatterns = [
    path('', front_page, name='front_page'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]