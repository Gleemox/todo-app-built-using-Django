from  django . shortcuts import render, redirect # redirect from one page to another
from django.contrib.auth.models import User # save user inputs into model
from todo.models import TODOO # save user inputs into model

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
    return render(request, 'loginn.html')