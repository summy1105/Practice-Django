from django.shortcuts import render

# Create your views here.

from .models import NewProject

def p_index(request):
  projects = NewProject.objects.all()
  context = {
    'projects' : projects
  }
  return render(request, 'newpractise/p_index.html', context)

def p_detail(request, pk):
  project = NewProject.objects.get(pk=pk)
  context = {
    'project' : project
  }
  return render(request, 'newpractise/p_detail.html', context)