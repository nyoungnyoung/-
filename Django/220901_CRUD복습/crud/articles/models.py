from re import L
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 생성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    
