from os import stat
from re import T
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def article_list(request):
  # 게시글 목록 JSON 주기!
  # 모델 객체를 쉽게 serialize 해주는 클래스가 있음!
  # >>> ModelSerializer
  # ModelForm이랑 비슷한 역할을 합니다. 
  # CRUD 할 때 데이터가 유효한가? 확인하는 기능
  # form.is_valid()>>>이런거 했었습니다..
  # articles = Article.objects.all()
  if request.method =='GET':
    articles = get_list_or_404(Article)
    serializer = ArticleSerializer(articles, many=True)
    # print(serializer.data)
    return Response(serializer.data)
  elif request.method == 'POST':
    #게시글 쓰기
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
  article = get_object_or_404(Article,pk=pk)
  if request.method == 'GET':
    # article = Article.objects.get(pk = pk)
    # 에러를 발생시키는게 아니라...없으면 없다라고 알려주기
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    # 업데이트 처리하기
    # 기존데이터 가지고 와서, 요청에서 데이터 받은걸로 업데이트하고
    serializer = ArticleSerializer(instance=article,data=request.data)
    # DB 적용하기 
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(data=serializer.data, status=status.HTTP_200_OK)
    # else:
    #   return Response(status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    # 삭제 처리하기
    # 기존 데이터 가지고 와서 
    # DB에서 삭제 
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 특정 게시글에 달린 댓글 전체 조회
def comments_list(request, article_pk):
  # article_pk를 이용해 게시글 조회
  # 게시글의 역참조를 통해 모든 댓글 조회할 수 있음
  # 
  pass