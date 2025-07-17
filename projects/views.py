from django.shortcuts import render
from . import models
# Create your views here.
def projects_lists_view(request):
    return render(request, 'projects/projects_lists.html')

def projects_lists_view(request):
    projects_lists = models.Project.objects.all()
    context = {
        'projects' : projects_lists
    }
    return render(request, 'projects/projects_lists.html', context)