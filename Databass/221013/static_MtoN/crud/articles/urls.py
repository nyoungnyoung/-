from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # index,
    # create/
    # <int:pk>/
    # <int:pk>/update/
    # <int:pk>/delete/
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 댓글 작성
    path('<int:article_pk>/comments/',
         views.comments_create, name='comments_create'),
    # 댓글 삭제
    path('<int:article_pk>/comments/<int:comment_pk>/delete',
         views.comments_delete, name='comments_delete'),
    # like 기능 구현
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
