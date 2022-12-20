from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

# Create your views here.
# login, logout, signup, delete, update,


@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인된 사용자는 로그인 사용못하게..
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        # 장고가 제공하는 로그인 기능을 사용해서 로그인하기
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:  # 로그인 하는 화면 보여주기 : 장고가 제공하는 로그인 폼을 사용
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인된 사용자면 회원가입 못하게 막음
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 회원가입도 로그인과 같이 회원가입 전용 form 이 있어요
    # UserCreationForm >> 바로 사용못해요 사용 클래스가...AbstractUser로만든 다른 User 클래스
    # UserCreationForm 재정의 해주기 accounts/forms.py
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 만약 회원가입후 바로 로그인 하게 하고 싶으면....
            # user = form.save()
            # auth_login(request,user)
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
