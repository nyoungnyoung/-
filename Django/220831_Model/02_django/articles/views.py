from django.shortcuts import render
from .models import Article

# Create your views here.


def index(request):
    # 데이터 베이스의 전체 데이터를 조회(Model import 해 와야 사용가능)
    # 같은 폴더 내에 있는 models.py에서 가져와야함!
    # .models(현재 위치에 있는 models에서) Article class를 import 해온다!
    articles = Article.objects.all()    # 전체 쿼리셋이 저장됨
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
