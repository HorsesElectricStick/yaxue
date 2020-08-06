from django.urls import path
from . import views

app_name = 'radar'
urlpatterns = [
    path('', views.school_list, name='school_list'),
    path('college/detail/<int:pk>/', views.detail, name='detail'),
    path('college/api/<int:pk>/', views.ajax_detail, name='ajax_api')
]