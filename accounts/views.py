from django.shortcuts import render

def Signup(request):
    return render(request,'accounts/Signup.html')

def Login(request):
    return render(request,'accounts/Login.html')

#def Logout(request):
#        return render(request,'accounts/Signup.html')
