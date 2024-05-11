from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>', views.index, name='paginated_quotes'),
    path('create/', views.create, name='create'),

]
