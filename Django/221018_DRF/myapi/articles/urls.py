
from django.urls import path,include
from . import views

urlpatterns = [
    path('articles/',views.article_list ),
    path('articles/<int:pk>/',views.article_detail),
    # 전체 댓글 
]