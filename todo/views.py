from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth import authenticate, login as Loginuser, logout as Logoutuser
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    user1 = request.user
    print(user1.id)
    if request.method == 'POST':
        
        new_todo = Todo( 
            user = request.user,
            title= request.POST['title'],
            description= request.POST['description'],
            status = request.POST['status'],
            priority= request.POST['priority']
        )
        new_todo.save()

        return redirect('/')
        
    if request.user.is_authenticated:
        user = request.user
        todos = Todo.objects.filter(user = user)
        return render(request, 'todo/index.html',{'todos': Todo.objects.filter(user = request.user.id),"user1":user})
    else:
        return redirect('signup')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            print('user not ',user)
            messages.success(request,f'Logged in Successfully!')
            if user is not None:
                Loginuser(request, user)
                request.session['user'] = request.user.id
                return redirect('index')
            
        else:
            context= {
                'form': form
            }
            return render(request,'todo/login.html',context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
    return render(request, 'todo/login.html', context)
    

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {
            "form": form,
        }

        return render(request, 'todo/signup.html',context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for { username } !')
            if user is not None:
                return redirect('login')
        else:
            context ={
                "form": form,
            }
            return render(request, 'todo/signup.html',context)
    return render(request, 'todo/index.html')


def delete(request,pk):
    delobj = Todo.objects.get(id=pk)
    delobj.delete()
    return redirect('/')


def logout(request):
    Logoutuser(request)
    return redirect('login')