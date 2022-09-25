from turtle import color
from unittest.util import _MAX_LENGTH
from django.shortcuts import render,redirect
from django.http import HttpResponse
from matplotlib.pyplot import cla
from .models import Register, Addmedicinenew

# Create your views here.

# def hello(request):
#     return HttpResponse("Hello welcome")
def pm(request):
    return render(request,'pm.html')

def Login(request):
    return render(request,'login.html')
def Signup(request):
    return render(request,'signup.html')
def Dashboard(request):
    return render(request,'dashboard.html')
def Noti(request):
    return render(request,'noti.html')
def Addmedicine(request):
    return render(request,'addmedicine.html')
def Addpatient(request):
    return render(request,'addpatient.html')
def Dmedicine(request):
    return render(request,'dmedicine.html')
def Hospital(request):
    return render(request,'hospital.html')
def Medicine(request):
    return render(request,'medicine.html')
def Patientlist(request):
    return render(request,'patientlist.html')
def Payment(request):
    return render(request,'payment.html')
def Search(request):
    return render(request,'search.html')
def Share(request):
    return render(request,'share.html')


def signupview(request):
   
    if request.method=='POST':

        model=Register()
        model.username=request.POST['username']
        model.email=request.POST['email']
        model.password=request.POST['password']
        model.save()
        return redirect('login')
  
    return render(request,'signup.html')




        


def Loginview(request):
    if request.method=='POST':
        try:
            m=Register.objects.get(email=request.POST['email'])
            if m.password==request.POST['password']:
                return redirect('dashboard')
            else:
                return render(request,'login.html',{'error':'INCORRECT PASSWORD'})
        except:
            return render(request,'login.html',{'error':'INCORRECT USERNAME' })
    return render(request,'login.html')

def addmedicineview(request):
   
    if request.method=='POST':

        model=Addmedicinenew()
        model.medicinename=request.POST['medicinename']
        model.medicineuse=request.POST['medicineuse']
        model.save()
        
  
    return render(request,'addmedicine.html')
