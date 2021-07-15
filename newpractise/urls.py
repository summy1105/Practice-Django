from django.urls import path

from . import views

app_name = 'newpractise'

urlpatterns = [
    path('', views.p_index, name='p_index'),
    path('<int:pk>/', views.p_detail, name='p_detail'),
    
]