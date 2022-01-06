from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from todo_maker.models import Task
from todo_maker.forms import TaskCreateForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class List(View):
    template = "todo_maker/list.html"

    def get(self, request, *args, **kwargs):
        instance = None
        if kwargs.get('pk', None):
            try:
                instance = Task.objects.filter(pk=kwargs.get('pk', None))[0]
            except Exception:
                instance = None

        # delete_id = kwargs.get('delete_id', None)
        
        if kwargs.get('pk', None):
            try:
                obj = Task.objects.filter(pk=kwargs.get('pk', None))[0]
                obj.delete()
                messages.add_message(request, messages.SUCCESS, "Task removed successfully.")
            except Exception:
                pass
                
        form = TaskCreateForm(instance=instance)
        context = {
            "tasks" : Task.objects.filter().order_by('task_accomplished'),
            "form" : form,
        }

        return render(request, self.template, context)
    
    def post(self, request, *args, **kwargs):
        instance = None
        post  = request.POST.copy()
        pk = post.get('id', None)
        
        msg = "New Task Created..."
        if pk:
            try:
                msg = "Task Updated..."
                instance = Task.objects.filter(pk=pk)[0]
            except Exception:
                instance = None

        form = TaskCreateForm(post, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.SUCCESS, msg)
        else:
            messages.add_message(request, messages.ERROR, "Please fill * marked fields")
            
        # url = reverse("todo_maker:list-todo")
        return redirect("todo_maker:list-todo")
