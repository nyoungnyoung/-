from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

import articles
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)



@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    # comment_form 에 CommentForm으로 요청받은 정보들 저장해주기
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():     # 유효성 검사 통과하면
        # comment.save()만 적으면 NOT NULL 오류 뜸(외래키값이 비었음)
        # article.pk값을 가져와주기 위해서 save의 commit 옵션을 False로 설정
        # -> 저장하지 않고 결과물로 나오는 인스턴스 값을 반환해줌
        comment = comment_form.save(commit=False)
        # comment가 몇번째 게시물에 저장되는지 설정해주기
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)


def comments_delete(request, article_pk, comment_pk):
    # 삭제할 댓글 조회(Comment 모델 import 해줘야함)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    # 오잉 detail로 redirect 하려면 article의 pk가 필요하겠네? 두가지 방법이 있다
    # 1. comment.article.pk로 comment에서 article 조회할 수 있음! 얘를 article_pk로 선언해서 얘를 그대로 사용
    # article_pk = comment.article.pk
    # 2. 애초에 urls.py에서 pk를 두개 받아주는 방법(variable routing)
    return redirect('articles:detail', article_pk)
