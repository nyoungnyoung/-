# 모델에 들어갈 데이터를 입력할 수 있는 폼 만들기
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    # fields = '__all__'
    exclude = ('user',) 

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ('article',)



