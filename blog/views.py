from django.shortcuts import render
from .models import Article

# Create your views here.
def blog(request):
    articles=Article.objects.all() 
    return render(request,'blog.html', context={'articles':articles})


def blog_detail(request,id):
    article=Article.objects.get(id=id)
    return render(request,'blog-detail.html', context={'article':article})


def example(request):
        users=[
        {'name':'orxan','age':27,'job': 'Sofware Developer'},
        {'name':'eli','age':24,'job': 'Sofware Developer'},
        {'name':'aysel','age':21,'job': 'Sofware Developer'},
        {'name':'senan','age':23,'job': 'Sofware Developer'},
        ]
        return render(request,'example.html',context={'users':users})
