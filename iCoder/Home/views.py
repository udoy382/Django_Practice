from django.db.models import query
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Home.models import Contact, Blog, Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# --------------------------------------------------------

# Django admin-panel
# username = Udoy
# password = 2299436

# --------------------------------------------------------

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # print(username, fullname, email, phone, password1, password2)

        if password1 != password2:
            messages.error(request, 'Oops! Your Password Does Not Match, Please Try-Again')
        
        elif len(password1 and password2) < 8:
            messages.error(request, 'Oops! Please Entered a Strong Password or greater then 8 Charector ')
        
        else:
            context = Contact(username=username, fullname=fullname, email=email, phone=phone, password1=password1, password2=password2)
            context.save()
            messages.success(request, "Your form has been submited!")


    return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    return render(request, 'blog.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}

    return render(request, 'blogpost.html', context)


def search(request):
    query = request.GET['query']

    if len(query) > 80:
        allPost = Blog.objects.none()
    else:
        allPostTitle = Blog.objects.filter(title__icontains=query)
        allPostContent = Blog.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent)

        params = {'allPost':allPost, 'query':query}

    return render(request, 'search.html', params)


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if  username.isalnum() == False:
            messages.error(request, "Oops! Please Use Small Latte in Username!")

        elif password1 != password2:
            messages.error(request, "Oops! Your Password Doesn't Match")

        elif len(password1 and password2) < 8:
             messages.error(request, 'Oops! Please Entered a Strong Password or greater then 8 Charector ')

        else:
            context = Signup(username=username, email=email, password1=password1, password2=password2)
            context.save()
            messages.success(request, "Your message hase been submited!")

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword1 = request.POST.get('loginpassword1')
        loginpassword2 = request.POST.get('loginpassword2')

        user = authenticate(loginusername=loginusername, loginpassword1=loginpassword1, loginpassword2=loginpassword2)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Loged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('home')

            
    return render(request, 'login.html')

def logout(request):
    return HttpResponse('This is a logut page')