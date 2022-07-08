from django.db.models import query
from django.shortcuts import render
from Home.models import Contact, allBlog
from django.contrib import messages


# Create your views here.

# ----------------------------------------------------
# Admin Panel~
# Username : Udoy
# Email : srudoy436@gmail.com
# Password : sr2299436
# ----------------------------------------------------

def home(request):
    blogs = allBlog.objects.all()
    context = {'blogs':blogs}

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        textarea = request.POST.get('textarea')

        # print(username, name, email, phone, password1, password2, textarea)

        if password1 != password2:
            messages.error(request, 'Oops! Your Password Does Not Match')

        elif len(password1 and password2) < 8:
            messages.error(request, 'Oops! Your Password Not Greater Then 8 Character')

        elif not username.islower():
            messages.error(request, 'Oops! Please Enter a Lower Case Username')

        else:
            context = Contact(username=username, name=name, email=email, phone=phone, password1=password1, password2=password2, textarea=textarea)
            context.save()
        
    return render(request, 'contact.html')

def blogPost(request, slug):

    blog = allBlog.objects.filter(slug=slug).first()
    second_context = {'blog':blog}

    return render(request, 'blogPost.html', second_context)


# Not warking Search Code
'''
def search(request):
    query = request.GET['query']

    if len(query) > 80:
        allPost = allBlog.objects.none()
    
    else:
        allPostTitle = allBlog.objects.filter(title__icontains=query)
        allPostContent = allBlog.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent)

        params = {'allPost':allPost, 'query':query}

    return render(request, 'search.html', params)
'''