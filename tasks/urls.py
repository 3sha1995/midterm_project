from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'), #lead to create
    path('<int:id>/edit/', views.task_update, name='task_update'), # lead to sa edit/update
    path('<int:id>/delete/', views.task_delete, name='task_delete'),# lead to sa delete confirmation
]
