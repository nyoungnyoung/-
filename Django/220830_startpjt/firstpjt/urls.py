"""firstpjt URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('처리할 URL/', 실행할 메서드),
    # articles/index
    # path('articles/index/', views.index),
    # path('greeting/', views.greeting),
    # path('lotto/', views.lotto),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('hello/<name>/', views.hello),
    # # pages/index
    # path('pages/index/', page_views.index)


    # articles/ >>> article.urls가 처리
    path('articles/', include('articles.urls')),
    # pages/ >>> pages.urls가 처리
    path('pages/', include('pages.urls')),

]
