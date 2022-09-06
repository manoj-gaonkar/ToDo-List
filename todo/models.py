from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    status_choices =[
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    task_priority= [
        ( '1', 'high'),
        ( '2', 'medium'),
        ( '3', 'low'),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField( auto_now_add=True )
    status = models.CharField(max_length=3, choices=status_choices)
    priority = models.CharField(max_length=5, choices=task_priority)

    def __str__(self):
        return self.title
    
