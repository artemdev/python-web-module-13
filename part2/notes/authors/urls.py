from . import views
from django.urls import path

app_name = 'authors'

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name='create'),
    path('<str:fullname>', views.show, name='show'),
]
