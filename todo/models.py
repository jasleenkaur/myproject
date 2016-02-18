from django.db import models
from django.utils import timezone
import datetime

class Todo(models.Model):
    tasks = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    status = models.BooleanField()
    
    def __str__(self):
        return self.tasks
    
