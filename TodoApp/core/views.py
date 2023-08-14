from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import TodoList
from django.contrib.auth.decorators import login_required


def Home(request):
    user = request.user.id
    todos = TodoList.objects.filter(user=user)
    
    context = {
        'todos':todos
    }
    return render(request, "index.html",context)


def SignUp(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["cnf_password"]
        
        if password ==  password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already exists!")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "User with this email already exsits!")
                return redirect("/register")
            else:
                user = User.objects.create_user(username =username, email=email, password = password)
                user.save()
                messages.info(request, f"{username}, you are successfully registered!")
                # user_login = authenticate(email = email, password = password)
                # login(request, user_login)
                return redirect("/")
        else:
            messages.info(request, "Password not matched!")
            return redirect("/register")
    else:
        return render(request, "register.html")


def SignIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # pwd = make_password(password)
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentals!")
            return redirect("/login")
    else:
        return render(request, "login.html")


@login_required(login_url="login")
def search(request):
    user = request.user.id
    if request.method == "POST":
        title = request.POST["title"]
        # print(title)
        title_object = TodoList.objects.filter(title__icontains = title, user=user)
        
        items = []
        for i in title_object:
            items.append(i)
        
        return render(request, "index.html", {'items':items})


@login_required(login_url="login")
def AddNewList(request):
    if request.method == "POST":
        curr_user = request.user.username
        title = request.POST["title"]
        items = request.POST["items"]
        
        user = get_object_or_404(User, username=curr_user)
        new_todList = TodoList.objects.create(title = title, items = items, user = user)
        new_todList.save()
        return render(request, "newList.html")
    else:
        return render(request, "newList.html")

@login_required(login_url="login")
def Todo(request,id):
    # print(id)
    todos = TodoList.objects.filter(pk = id)
    # print(todos)
    context = {
        'todos':todos,
        # 'items':items
    }
    return render(request, "todo.html", context)

@login_required(login_url="login")
def updateTodo(request, id):
    user = request.user.username
    data = TodoList.objects.get(pk = id)
    if request.method == "POST":
        data.title = request.POST["title"]
        data.items = request.POST["items"]
        if "checked" in request.POST:
            data.completed = True
        else:
            data.completed = False
        data.save()
        return redirect("/todoitem/"+str(id))
    else:
        context = {
            'data':data
        }
        return render(request, "todo.html", context)

@login_required(login_url="login")
def deleteTodo(request,id):
    todos = TodoList.objects.get(pk = id)
    todos.delete()
    return redirect("/")

@login_required(login_url="login")
def SignOut(request):
    logout(request)
    return redirect("/")