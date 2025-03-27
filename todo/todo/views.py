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


def todo(request):
    if request.method == 'POST': # POST in capital letters
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title,user=request.user) # get the todo object related to the logged in user from database
        obj.save() # save this object in our model TODOO
        user=request.user        
        res=models.TODOO.objects.filter(user=user).order_by('-date') # get all the logged in user's todo list items ordered by date
        return redirect('/todopage',{'res':res}) # sens this user's todo list to todo page to show it on this page
        
    
    res=models.TODOO.objects.filter(user=request.user).order_by('-date') # res in used in todo.html to loop and show todo list items on todo page
    return render(request, 'todo.html',{'res':res,}) # save res object in todo.html file



def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO.objects.get(srno=srno) # search for todo item by id passed in parameters
        obj.title = title # change old title to new titile
        obj.save() # save object
        return redirect('/todopage')

    obj = models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})