# todolist/urls.py
from django.conf.urls import url
from todolist import views


urlpatterns = [
    url(r'^$', views.index, name = 'todolist'),
]