from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Contact

# Create your views here.

# -----------------------------------------------------

# Admin Panel~
# Username : Udoy
# Password : udoy123

# -----------------------------------------------------

def home(request):
    # return HttpResponse('This is a Home page')

    return render(request, 'home.html')

def about(request):
    # return HttpResponse('This is a about page')

    return render(request, 'about.html')

def contact(request):

    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        textarea = request.POST.get('textarea')

        if password1 != password2:
            messages.error(request, "Oops! Your Password Doesn't Match")

        elif len(password1 and password2) < 8:
            messages.error(request, "Oops! Your Password Not a 8 or More Charector ")

        else:

        # print(username, name, email, password1, password2, textarea)

            context = Contact(username=username, name=name, email=email, password1=password1, password2=password2, textarea=textarea)
            context.save()

    # return HttpResponse('This is a contact page')

    return render(request, 'contact.html')

def search(request):
    # return HttpResponse('This is a Search page')

    return render(request, 'search.html')