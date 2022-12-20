from django.urls import path
from pages import views



urlpatterns = [
  # pages/index
    path('index/', views.index, name='index')
]