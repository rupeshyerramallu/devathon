from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse
from .models import Guest, Registered
def index(request):
    return render(request, 'home/guard-base.html')
    return HttpResponse("<h1>Hello</h1>")

def inout(request):
    if request.method=="POST":
        if request.POST['direction']=='1':
            a=Guest()
            a.num=request.POST['num']
            a.entry=datetime.now()
            a.exit=datetime.now()
            a.flag=1
            a.save()
            return render (request,'home/guard-base.html',{'success':'Succesful'})
        else:
            return HttpResponse("<h1>Not 1 direction</h1>")
    else:
         return HttpResponse("<h1>not-post-method</h1>")


def log(request):
    return render(request,'home/login.html')
    return HttpResponse("<h1>Hello</h1>")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and  user.is_superuser :
            if user.is_active:
                login( request , user)

                return render(request, 'home/admin-base.html')

            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        if user is not None and not user.is_superuser:
            login(request,user)
            return render(request, 'home/guard-base.html')
    else:
        return render(request, 'home/login.html')


def register(request):
    if request.method == "POST":
        a = Registered()
        a.num=request.POST['num']

        a.save()
        return HttpResponse("<h1>success</h1>")

    else:
        return HttpResponse("<h1>not_succes</h1>")


def adview(request):
    if request.user.is_authenticated():
        vehicles = Guest.objects.filter( Q(flag=1) )
        return render(request,'home/admin-view.html',
        {
        'vehicles': vehicles, 'number': Guest.objects.filter(flag=1).count()})
    else:
        return HttpResponse("<h1>abcd</h1>")


def log_out(request):
    logout(request)
    return render(request, 'home/login.html', )
