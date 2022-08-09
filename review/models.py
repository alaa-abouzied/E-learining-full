from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Review(models.Model):
    description = models.CharField(max_length=1000, null=True)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self):
        return f"{self.description}"