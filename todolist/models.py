from django.db import models

# Create your models here.
class Todolist(models.Model):
    Title = models.CharField(max_length=10)
    description =models.TextField()
    state = models.BooleanField(default=False)
    time_of_completion= models.DateTimeField(null = True, blank= True)
       