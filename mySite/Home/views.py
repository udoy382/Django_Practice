from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Contact
from Home.models import Blog
from django.contrib import messages

# Create your views here.

# --------------------------------------------------------

# django-admin username and password
"""
Username = Udoy
Email = srudoy436@gmail.com
Password = sr2299
"""
# --------------------------------------------------------

def home(request):
    # return HttpResponse('This is a home page')

    return render(request, 'home.html')

def about(request):
    # return HttpResponse('This is a about page')

    return render(request, 'about.html')

def contact(request):
    # return HttpResponse('This is a contact page')

    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # print(name, username, email, password1, password2)

        if len(password1 and password2) < 8:
            messages.error(request, "Make sure your password is at lest 8 letters")
        
        elif password1 != password2:
            messages.error(request, "Your password does't match: Please try again!")

        else:
            context = Contact(name=name, username=username, email=email, password1=password1, password2=password2)
            context.save()
            messages.success(request, "Your form has been submited!")

    return render(request, 'contact.html')


def blog(request):
    # return HttpResponse('This is a blog page')
    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    # return HttpResponse('This is a blog page')
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}

    return render(request, 'blogpost.html', context)
