from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        # 로그인 처리하기
        # 사용자가 보낸 id/password 받아와서 >>> AuthenticationForm 만들고 로그인 처리
        # 로그인 처리) 아이디 존재하는지 확인하고,,, 비밀번호 비교하고... 일치하면 세션에 담아주고.. 일치하지 않으면 또 다른 작업하고...
        # 이런 번거로운 작업을 쟝고가 들고있는 login함수가 알아서 해준다!(이름이 겹쳐서 다른 이름으로 바꿔서 import)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        # 로그인 화면 보여줘(얘도 폼이다!)
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        # request에 회원가입 정보가 있을거에요
        # 받아와서 회원가입하기
        # 회원가입 어떻게 하나요?? DB에 저장하면 됨! .save()
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 자동으로 로그인
            # auth_login(request, user)
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/signup.html',context)