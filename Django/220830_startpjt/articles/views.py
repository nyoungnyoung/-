from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.
# 첫번째 인자는 request, 반환값은 HttpResponse
# render 함수의 역할 : template를 이용해 HttpResponse를 만들어냄
# render(request, 템플릿 경로[, context(=data)])
def index(request):
    # 템플릿에 data를 전달 할 때는 dictionary 형태로 전달!
    context = {
        # key : value
        'msg' : list('HELLO')
    }
    return render(request, 'index.html', context)

def greeting(request):
    return render(request, 'greeting.html', {'name' : 'Alice'})


def lotto(request):
    target = list(range(1, 46))
    numbers = sorted(random.sample(target, 6))
    context = {
        'numbers': numbers
    }
    return render(request, 'lotto.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # 클라이언트가 보낸 데이터를 받아서
    message = request.GET.get('message')
    #  템플릿으로 보내야함
    context = {
        # 클라이언트가 보낸 데이터를 담아주면 됨
        'message' : message
    }
    return render(request, 'catch.html', context)

# variable routing을 통해 받아온 값을 템플릿으로 넘기기
def hello(request, name):
    context = {
        'name' : name
    }
    return render(request, 'hello.html', context)