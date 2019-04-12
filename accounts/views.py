from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def Signup(request):
    if request.method == 'POST':
        if request.POST['Pass'] == request.POST['ConfPass']:
            try:
                user = User.objects.get(Username=request.POST['Username'])
                return render(request, 'accounts/Signup.html', {'error': 'Username has already been taken!'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['Username'],Password=request.POST['Pass'],Email=request.POST['Email'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/Signup.html', {'error': 'Passwords must match!'})
    else:
        return render(request,'accounts/Signup.html')


def Login(request):
    if request.method == 'POST':
        user= auth.authenticate(Username=request.POST['Username'],Password=request.POST['Pass'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/Login.html',{'error': 'Invalid Username or Password!'})        
    else:
        return render(request,'accounts/Login.html')


#def Logout(request):
#        return render(request,'accounts/Signup.html')
