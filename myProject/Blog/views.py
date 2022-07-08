from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Blog

# Create your views here.


def blogHome(request):

    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    # return HttpResponse('This is a blogHome page')

    return render(request, 'blogHome.html', context)

def blogPost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}

    # return HttpResponse('This is a blogPost page')

    return render(request, 'blogPost.html', context)