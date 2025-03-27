from  django . shortcuts import render, redirect # redirect from one page to another
from django.contrib.auth.models import User # save user inputs into model
from todo.models import TODOO # save user inputs into model
from todo import models
from django.contrib.auth import authenticate, login, logout # authenticate or user login

# sign up page
def signup(request):
    if request.method == 'POST': # get user inputs and save them in the model
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd) # username, user email, password
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save() # save model
        return redirect('/loginn') # redirect user to login page
    
    return render(request, 'signup.html')


def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd) # authentification 
        if userr is not None:
            login(request,userr)
            return redirect('/todopage') # if the user exists in the DB show todo page
        else:
            return redirect('/loginn') # else stay in login page
               
    return render(request, 'loginn.html')