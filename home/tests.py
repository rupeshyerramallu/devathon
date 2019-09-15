from django.test import TestCase





def inout(request):
    if  not request.user.is_authenticated() :
        return render(request, 'home/login.html')
    if request.method=="POST":
        objdata=Registered.object.all()

        fl=1
        for obj in objdata:
            if obj['num']==request.POST['num']:
                fl=0


         if fl==0
         return render(request, 'home/guard-base.html', {'success': 'already in registered vehicles'})


        if request.POST['direction']=='1':
            a=Guest()
            a.num=request.POST['num']
            a.entry=datetime.now()
            a.exit=datetime.now()
            a.flag=1
            a.save()
            return render (request,'home/guard-base.html',{'success':'Succesful'})
        else:
            a=Guest.fil

    else:
        return render(request, 'home/login.html')



























def inout(request):
    if  not request.user.is_authenticated() :
        return render(request, 'home/login.html')
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
            return render(request, 'home/guard-base.html', {'success': 'Succesful'})
    else:
        return render(request, 'home/login.html')

