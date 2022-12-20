from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # 게시글 삭제 : 어떤 댓글을 삭제할지 pk는 필요할 것 같은데, 어떤 게시물인지 pk도 필요할까?
    # path('<int:comment_pk>/comments/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    # 이렇게 하는 이유? variable routing 사용하는 애들은 전부 article_pk로 주소가 시작함(일관성을 위해)
]
