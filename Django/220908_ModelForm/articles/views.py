from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.

@require_safe
def index(request):
  # 게시글 전체 목록 가져와서 화면에 보여주기
  articles = Article.objects.all()
  context = {
    'articles' : articles
  }
  return render(request,'articles/index.html',context)

# def new(request): # 새 글쓰기 화면 보여주기
#   #form 인스턴스를 활용한 그림 그리기
#   form = ArticleForm()
#   context = {
#     'form' : form
#   }
#   return render(request,'articles/new.html',context)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):    # method가 GET / POST 외에도 있기 때문에, GET과 POST의 위치를 바꿔서는 안됨!!(POST 요청일때 DB가 바뀌기 때문)
  if request.method == "POST":
    form = ArticleForm(request.POST)
    # 제대로된 데이터라면 저장!
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = ArticleForm()

  # form 인스턴스는 뭐가 잘못됬는지 알고있음!
  # print(form.errors)
  context = {
    'form' : form
  }
  return render(request,'articles/create.html',context)

@login_required
@require_safe
def detail(request, pk):
  # 게시글 하나 선택해서 상세화면 보여주기
  # DB에서 게시글 하나 가져오기 
  article = Article.objects.get(pk=pk)
  context = {
    'article' : article
  }
  return render(request,'articles/detail.html',context)

# def edit(request,pk):
#   # 수정화면 보여주기, 기존에 데이터를 화면에 표시해줘야 함
#   article = Article.objects.get(pk = pk)
#   context = {
#     'article' : article
#   }
#   return render(request,'articles/edit.html',context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request,pk):
  article = Article.objects.get(pk = pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm(instance=article)
  context = {
    'form' : form,
    'article' : article,
  }
  return render(request, 'articles/update.html', context)

@login_required
@require_POST
def delete(request,pk):
  if request.method == 'POST':
    article = Article.objects.get(pk=pk)
    article.delete()
  return redirect('articles:index')