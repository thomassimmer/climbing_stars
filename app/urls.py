from django.urls import path
           
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:path_id>/detail/', views.detail, name='detail'),
    path('new_path/', views.new_path, name='new_path'),
]
