

from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    # path('new/',views.new,name='new'),  # 새 글 작성 화면 보여줘
    path('create/',views.create,name='create'),  # 새 글 작성 저장 해줘
    path('<int:pk>/detail/',views.detail, name='detail'),  # 상세 화면 보기
    # path('<int:pk>/edit/',views.edit, name='edit'),  # 수정 화면 보여줘
    path('<int:pk>/update/',views.update, name='update'),  # 수정 해줘
    path('<int:pk>/delete/',views.delete, name='delete'),  # 수정 해줘
]
