from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from role.models import Role

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            role = Role.objects.get(user=user)
            request.session['rolename'] = role.rolename
            return redirect('home')
        else:
            print("error")
    context= {
        "form":form
    }
    return render(request,"login.html",context)

def home_page(request):

    return render(request,"base.html",{})

def logout_page(request):
    logout(request)
    return redirect("login")

def contact_page(request):
    return render(request,"contact.html",{})

def dept(request):
    return render(request,"dept.html",{})
