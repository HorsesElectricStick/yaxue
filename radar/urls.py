from django.urls import path
from . import views

app_name = 'radar'
urlpatterns = [
    path('', views.school_list, name='school_list'),
    path('college/detail/<int:pk>/', views.detail, name='detail'),
    path('college/detail_api/', views.ajax_detail, name='detail_api'),
    path('college/search_api/', views.ajax_search, name='search_api')
]