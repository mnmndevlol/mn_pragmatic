from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request): # 리퀘스트 필수인자이고 리퀘스트를받아서 리스폰스로 되돌려줌
    return HttpResponse('Hello World!')