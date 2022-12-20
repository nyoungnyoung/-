# 사용자에게 보여줄 Form 모양 선언
# django Form을 상속받아서 작성
from dataclasses import field
from tkinter import W, Widget
from django import forms
from .models import Article

# 요 클래스의 목적 : 템플릿에서 폼 그리기
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(
#         label = '내용',
#         widget=forms.Textarea(
#                 attrs= {
#                     'placeholder' : '내용을 입력하세요.'
#                 }
#             )
#         )
#     )
# 위 form은 모델과 상관없이 내용을 작성한것...
# 만약에 모델이 가진 필드들과 동일하게 내용을 작성해야 한다면?
# Model참고하면 쉽게 작성 가능하겠는데?? >>> MOdelForm

class ArticleForm(forms.ModelForm):
    # 필드 만들때... 모델꺼 참고해서 만들면 됨!
    class Meta:
        model = Article
        # 사용할 필드에 대한 선언
        fields = '__all__'
        # fields = ['title', 'content']