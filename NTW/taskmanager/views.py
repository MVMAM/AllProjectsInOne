from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'taskmanager/index.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})


def about(request):
    return render(request, 'taskmanager/about.html')


def creator(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_of_taskmanager")
        else:
            error = "Форма была неверной"

    form = TaskForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'taskmanager/creator.html', context)


def info(request):
    return render(request, 'taskmanager/info.html')


class TaskmanagerDetailView(DetailView):
    model = Task
    template_name = "taskmanager/details_view.html"
    context_object_name = "task"


class TaskmanagerUpdateView(UpdateView):
    model = Task
    template_name = "taskmanager/updator.html"

    form_class = TaskForm


class TaskmanagerDeleteView(DeleteView):
    model = Task
    success_url = "/taskmanager/"
    template_name = "taskmanager/deletor.html"