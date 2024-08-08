from django.views.generic import ListView
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    

def task_list(request):
    tasks=Task.objects.all().values('id','title','created_at')
    return JsonResponse(list(tasks),safe=False)

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_task = Task.objects.create(title=data['title'], description=data.get('description', ''))
        return JsonResponse({'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'completed': new_task.completed})

@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'result': 'Task deleted'})

@csrf_exempt
def update_task(request, task_id):
    if request.method == "PATCH":
        data = json.loads(request.body)
        task = Task.objects.get(id=task_id)
        task.completed = data.get('completed', task.completed)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.save()
        return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed})