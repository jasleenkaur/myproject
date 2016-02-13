from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    post_content = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    pub_date = models.DateTimeField(blank = True)
    
    def __str__(self):
        return self.title
    
