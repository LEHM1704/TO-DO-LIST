from django.urls import path
from . import views

urlpatterns = [
    path('',views.TaskListView.as_view(),name='task_list'),
    path('api/task/',views.task_list,name='api_task_list'),
    path('api/tasks/add/', views.add_task, name='add_task'),
    path('api/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('api/tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    
]
