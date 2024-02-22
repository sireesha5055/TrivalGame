from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
def wel(request):
    return HttpResponse("<h1 style ='text-align :center ; border:1px solid green ; background-color:gold'> Welocme to my application")
def Home(request):
    return HttpResponse("<h2>welcome</h2>")
def hai(request):
    return render(request,"hai.html",{})
def hai_vars(request):
    eid = 101
    ename = 'siri'
    esal = 17000000
    return render(request,"vform.html",{'eid': eid,'ename': ename,'esal': esal})

def emp(request):
    template= loader.get_template("empform.html")
    context={
    'ename':'k.sireesha',
    'dname':'mlc',
    'sub':'politics',
    }
    return HttpResponse(template.render(context,request))
def dept(request, dname,dno,dlocation):
    return render(request,"dform.html",{'dname':dname,'dno':dno ,'dlocation':dlocation})

def form_submit(request):
    if request.method=='POST'
    uname=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    if uname ==
     

   