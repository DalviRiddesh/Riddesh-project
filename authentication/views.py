from gzip import FNAME
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    return render(request, "authentication/index.html")
 
def signup(request):

    if request.method == "POST":
       # username = request.Post.get('username')
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            myuser= User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.lname_name = lname
            
            myuser.save()

            messages.success(request,"your account has sucessfully created.")

            return redirect('signin')

    return render(request, "authentication/signup.html")




def signin(request):

        if request.method == 'POST':
            Username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=Username, password=pass1)
            print(request.user)
            if user is not None:
                login(request,user)
                fname = user.first_name
                return render(request,"authentication/index.html",{'fname': fname})
            else:
                messages.error(request,"Bad credentials")
                return redirect('signin')
            



        return render(request, "authentication/signin.html")



def signout(request):
    return render(request, "authentication/signin.html")
    
