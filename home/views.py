from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse
from .models import Guest, Registered
from datetime import datetime, timedelta
def index(request):
    return HttpResponse("<h1>Hello</h1>")

def inout(request):
    if  not request.user.is_authenticated() :
        return render(request, 'home/login.html')
    if request.method=="POST":
        objdata = Registered.objects.all()

        fl=1
        for obj in objdata:
            if obj.num == request.POST['num']:
                fl=0
                print("hello")


        if fl == 0 :
            return render(request, 'home/guard-base.html', {'success': 'already in registered vehicles'})


        if request.POST['direction']=='1':
            a=Guest()
            a.num=request.POST['num']
            a.entry=datetime.now()
            a.exit=datetime.now()
            a.flag=1

            objec =Guest.objects.filter( Q(flag=1),Q(num=request.POST['num']) )
            k1=1
            data = 'Succesful'
            c= objec.count()
            if c > 0 :
                kl=0
                data='Error: This vehicle previously Did not exit'

            if k1==1:
                a.save()

            return render (request,'home/guard-base.html',{'success':data})
        else:


            obje = Guest.objects.filter(Q(flag=1), Q(num=request.POST['num']))
            b1 = 1
            data = 'Succesful'
            c = obje.count()
            if c == 0:
                b1 = 0
                data = 'Error: This  vehicle previously Did not Enter'
                print(data)
            if b1 == 1:
                a = obje[0]
                a.flag = 2
                a.save()

            return render(request, 'home/guard-base.html', {'success': data})


    else:
        return render(request, 'home/login.html')

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
                r_vehicles = Registered.objects.all()
                g_vehicles = Guest.objects.filter(flag=1)
                print(r_vehicles.count())
                print(g_vehicles.count())

                return render(request, 'home/admin-base.html', {
                    'r_vehicles': r_vehicles, 'r_number': Registered.objects.all().count(),
                    'g_vehicles': g_vehicles, 'g_number': Guest.objects.filter(Q(flag=1)).count()}
                              )


            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        if user is not None and not user.is_superuser:
            login(request, user)
            return render(request, 'home/guard-base.html')

        if user is None:
            return render(request, 'home/login.html', {'error_message': 'Invalid Login'})
    else:
        return render(request, 'home/login.html')

def register(request):
    r_vehicles = Registered.objects.all()
    g_vehicles = Guest.objects.filter(flag=1)


    if request.method == "POST":
        a = Registered()
        a.num=request.POST['num']
        objdata = Registered.objects.all()
        data1 = 'Succesful'
        data2 = 'UnSuccesful : Already Present'
        data = data1
        fl=1
        for obj in objdata:
            if obj.num == request.POST['num']:
                data=data2
                fl=0
        if fl==1:
            a.save()
        return render(request, 'home/admin-base.html', {
            'r_vehicles': r_vehicles, 'r_number': Registered.objects.all().count(),
            'g_vehicles': g_vehicles, 'g_number': Guest.objects.filter(Q(flag=1)).count(),
            'success': data}
                      )

    if request.user.is_authenticated():
        return render(request, 'home/admin-base.html', {
        'r_vehicles': r_vehicles, 'r_number': Registered.objects.all().count(),
        'g_vehicles': g_vehicles, 'g_number': Guest.objects.filter(Q(flag=1)).count()}
                  )


    return render(request, 'home/login.html')

def adview(request):
    if request.user.is_authenticated():
        vehicles = Guest.objects.filter( entry__lte = datetime.now()- timedelta(days=0.1)).filter( Q(flag=1))
        return render(request,'home/admin-view.html',
        {
        'vehicles': vehicles, 'number': Guest.objects.filter(entry__lte = datetime.now()- timedelta(days=0.1)).filter( Q(flag=1)).count()})
    else:
        return render(request, 'home/login.html')



def log_out(request):
    logout(request)
    return render(request, 'home/login.html')
