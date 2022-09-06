from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    if request.method == 'POST':
        new_todo = Todo( 
            title= request.POST['title']
        )
        new_todo.save()

        return redirect('/')
    return render(request, 'todo/index.html',{'todos': Todo.objects.all()})

def delete(request,pk):
    delobj = Todo.objects.get(id=pk)
    delobj.delete()
    return redirect('/')
