from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.

def index(request):
    posts = Posts.objects.all()[:10] #top 10
    result={
        'title':'Latest Posts!',
        'posts':posts
    }
    return render(request,'posts/index.html',result)


def details(request,id):
    post = Posts.objects.get(id=id)
    result={
        'post':post
    }
    return render(request,'posts/details.html',result)