from django.urls import path 
from . import views as v

urlpatterns = [
    path('', v.Home),
    path('login', v.SignIn, name="login"),
    path('register', v.SignUp, name="register"),
    path('search', v.search, name="search"),
    path('add_todos', v.AddNewList, name="add-todos"),
    path('todoitem/<int:id>', v.Todo),
    path('todoitem/updatetodo/<int:id>', v.updateTodo),
    path('deletetodo/<int:id>', v.deleteTodo),
    path('logout', v.SignOut, name="logout"),
]
