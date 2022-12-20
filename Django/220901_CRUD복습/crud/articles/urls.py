"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),    # 새 글 작성 화면 보여줘
    path('create/', views.create, name='create'),    # 새 글 작성 저장
    path('<int:pk>/detail/', views.detail, name='detail'),    # 상세 화면 보여줘
    path('<int:pk>/edit/', views.edit, name='edit'),   # 수정 화면 보여줘(기존 게시물의 내용이 보여져야함 : pk 필요)
    path('<int:pk>/update/', views.update, name='update'),   # 수정해줘(기존 게시물의 내용을 수정해야함 : pk 필요)
    path('<int:pk>/delete/', views.delete, name='delete'),
]
