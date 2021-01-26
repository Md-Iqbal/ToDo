from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo_model(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank = True)
    Important = models.BooleanField(default = False)
    Created_time = models.DateTimeField(auto_now_add=True)
    Completed_time = models.DateTimeField(null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Title
    
