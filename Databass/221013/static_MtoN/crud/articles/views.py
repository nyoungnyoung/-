from cgitb import reset
import imp
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.


@require_safe
def index(request):
    # database에서 게시글 목록 가져온 다음에 템플릿에 보내주기
    # 모델 클래스의 objects 매니저를 이용해서 데이터 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


@login_required
@require_safe
def detail(request, pk):
    # pk를 이용해 DB 조회하고, context에 담아서 전달
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 게시글을 이용해서 댓글에 참조하기 > 역참조 : 역참조 매니저 이용 : 매니저 이름: comment_set
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:  # 요청이 POST가 아님, 수정화면 보여주기
            form = ArticleForm(instance=article)

    else:  # 게시글 작성자와 로그인된 사용자가 다름
        return redirect('articles:index')

    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        if article.user == request.user:
            article.delete()
    return redirect('articles:index')


@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # comment_form.save() >>> article이 참조되지 않음 NOT NULL constraint error
            # commit=False DB에 저장하지 않고 comment객체를 얻어옴
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

        return redirect('articles:detail', article_pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)


@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
