from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    photo=models.ImageField(blank=True, null=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post)
    author=models.CharField(max_length=20)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


