from multiprocessing import context
from urllib import request
from xmlrpc.client import DateTime
from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render (request,('index.html'))

def all_emp(request):
    emps = Employee.objects.all()
    context ={
        "emps": emps
    }
    print(context)
    return render (request, 'view_all_emp.html' ,context)

def add_emp(request):
    if request.method =="POST":
        print("post")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = int(request.POST.get('dept')) 
        role = int(request.POST.get('role')) 
        salary = int(request.POST.get('salary')) 
        bonus = int(request.POST.get('bonus')) 
        phone = int(request.POST.get('phone')) 
        add_emp=Employee(first_name=first_name,last_name=last_name, dept_id=dept, role_id=role, salary=salary, bonus=bonus, phone=phone, hire_date=datetime.now())
        print(add_emp)
        add_emp.save()
  
        return render( request,'add_an_emp.html')
    elif request.method=='GET':
         return render(request,'add_an_emp.html')
    else:
         print('error')
         return HttpResponse('Exception error!')
        
    
   

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed =Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return render(request,'index.html')
        except:
            pass
           # return HttpResponse('Enter a Valid Employee ID')
    
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render (request,'remove_an_emp.html',context)

def filter_emp(request):
    if request.method  =='POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps =Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains = dept)
           
        if role :
            emps=emps.filter(role__name__icontains =role)
            
        context ={
            'emps':emps
        }
        return render(request,'view_all_emp.html', context)
    elif request.method =="GET":
        return render (request,     'filter_an_emp.html')
    else:
        return HttpResponse('Error')
