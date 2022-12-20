from django.urls import path
# 명시적 상대경로(현재 '.'폴더 안에 있는 views를 가져오겠다!!)
from . import views

# 당장 path를 쓰지 않더라도 urlpatterns는 작성해야 함
# firstpjt의 urls.py를 먼저 거쳐오기 때문에, 여기서 index/만 작성해도
# pages/index/로 인식하게 됨!!

# 앱이름은 항상 app_name이라는 변수명으로 선언해 줄 것!
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
