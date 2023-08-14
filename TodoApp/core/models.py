from django.db import models
from django.contrib.auth.models import User
import pickle


class TodoList(models.Model):
    title = models.CharField(max_length=255,default='')
    items = models.TextField(max_length=300, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'TodoList'
    
    def __str__(self):
        return self.title

# class Items(models.Model):
#     items = models.CharField(max_length=255)
#     todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.items

