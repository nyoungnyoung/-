from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculation.html')

def result(request):
    context= {'A' : request.GET.get('A'),
    'B' : request.GET.get('B')}
    return render(request, 'result.html', context)