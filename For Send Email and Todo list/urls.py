from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('todolist/', Todolist , name='todolist'),
    path('contact/', Contact , name='contact'),
]
