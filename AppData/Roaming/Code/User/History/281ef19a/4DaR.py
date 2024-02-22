from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
def wel(request):
    return HttpResponse("<h1 style ='text-align :center ; border:1px solid green ; background-color:gold'> Welocme to my application")
def Home(request):
    return HttpResponse("<h2>welcome</h2>")
def hai(request):
    return render(request,"hai.html",{ })
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
def test1(request):
    template=loader.get_template("hform.html")
    return HttpResponse(template.render())
def test2(request):
    template=loader.get_template("home.html")
    context={
        'uname':'sireesha',
        'pass':'sireesha123', }
    return HttpResponse(template.render(context,request))

def test3(request):
    template=loader.get_template("susform.html")
    return HttpResponse(template.render())

def test4(request):
    template=loader.get_template("fform.html")
    return HttpResponse(template.render())

def login(request):
    return render(request,"login.html",{})


def form_submit(request):
    if request.method=='POST':
         uname=request.POST.get('uname')
         pwd=request.POST.get('pwd')
    if uname =='admin' and pwd =='admin':
         return render(request,"sus.html",{'uname':uname ,'pwd':pwd})
    else:
         return render(request,"fail.html",{})



def test_for(request):
    template=loader.get_template("fform2.html") 
    context={
        'emps':[
            {'eid':'101','enmae':'ravi','esal':'1900000','deptno':'1'},
            {'eid':'102','enmae':'rani','esal':'130000','deptno':'2'},
            {'eid':'103','enmae':'rajesh','esal':'450000','deptno':'3'},
            {'eid':'104','enmae':'rama','esal':'600000','deptno':'4'},
        ],
    }
    return HttpResponse(template.render(context,request))
       


   