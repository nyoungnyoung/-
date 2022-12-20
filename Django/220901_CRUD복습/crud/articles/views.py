from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 목록 가져와서 화면에 보여주기
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


def new(request):   # 새 글쓰기 화면 보여주기
    return render(request, 'articles/new.html')


def create(request):    # 글 저장하고 나서 index화면 보여주기
    # 요청 시에 사용자가 보낸 데이터를 받아서 DB에 저장하기
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # create 요청이 직접 화면을 그려주는게 아니라, 브라우저한테
    # 보여주고 싶은 화면을 다시 요청하라고 응답
    return redirect('articles:index')


def detail(request, pk):        # urls.py 내의 path변수에 입력되는 <int:pk>를 매개변수로 받기
    # 게시글 하나 선택해서 상세화면 보여주기
    # DB에서 게시글 하나 가져오기
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    # 수정화면 보여주기(render필요함)
    # 기존 데이터를 화면에 표시해줘야 함
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # DB에 수정내용 적용하기(화면 보여주는 요청 X -> render 필요없음, redirect사용!)
    # 기존의 article 가져와서, 클라이언트가 나한테 준 데이터로 바꿔주고 save
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')