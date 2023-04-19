from django.shortcuts import render
from learn_site.models import Project, Task

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects, 'title': 'Projects'})

def task(request, pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks.html', {'project': project, 'tasks': tasks, 'title': 'Tasks'})
