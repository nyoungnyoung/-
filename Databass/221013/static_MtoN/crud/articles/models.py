from django.db import models
from django.conf import settings
# from accounts.models import User
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(blank=True)

    def __str__(self):
      return self.title

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete = models.CASCADE)
  content = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True) 
  
