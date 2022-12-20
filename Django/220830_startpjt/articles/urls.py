from django.urls import path
from articles import views
app_name='articles'

urlpatterns = [
    # articles/index
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('lotto/', views.lotto),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<name>/', views.hello),
]