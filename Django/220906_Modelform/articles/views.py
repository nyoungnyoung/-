from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():     # 유효성 검사 통과하면
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:       # 데코레이터 사용하고나면 요 부분이 GET일때로 한정됨!
        # new
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)



    # form = ArticleForm(request.POST)
    # if form.is_valid():     # 유효성 검사 통과하면
    #     article = form.save()
    #     return redirect('articles:detail', article.pk)
    # # print(f'에러: {form.errors}')
    # # 여기로 넘어왔다는건 유효성검사 실패했다는 뜻
    # context = {
    #     'form' : form
    # }
    # return render(request, 'articles/new.html', context)
    # return redirect('articles:new')     # 통과 못하면
    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST   # POST일때만 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form
#     }
#     return render(request, 'articles/edit.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # update
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # edit
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form
    }
    return render(request, 'articles/update.html', context)



    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article)
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail', article.pk)
    # context = {
    #     'form' : form,
    # }
    # return render(request, 'articles/edit.html', context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)