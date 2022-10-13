from django.urls import path
from todolist.views import front_page, register, login_user, logout_user
from todolist.views import create_task, delete_task, get_todolist_json, create_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', front_page, name='front_page'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/<str:pk>', delete_task, name='delete_task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', create_task_ajax, name='create_task_ajax'),
]