from django.http import HttpResponse
from django.shortcuts import render,redirect
import joblib
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required(login_url='/login/')
def heart(request):
    return render(request,'heart.html')
@login_required(login_url='/login/')
def diabetes(request):
    return render(request,'diabetes.html')
def result_diabetes(request):
    classifier=joblib.load('finalized_model1.sav')
    li=[]

    li.append(request.GET['pregnancies'])
    li.append(request.GET['Glucose'])
    li.append(request.GET['Blood pressure'])
    li.append(request.GET['skin Thikness'])
    li.append(request.GET['Insulin'])
    li.append(request.GET['BMI'])
    li.append(request.GET['DiabetesPedigreeFunc.'])
    li.append(request.GET['Age'])

    ans=classifier.predict([li])
    return render(request,'result_diabetes.html',{'ans':ans})

def result_heart(request):
    lr=joblib.load('finalized_model.sav')
    lis=[]

    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['chestpain'])
    lis.append(request.GET['bloodpressure'])
    lis.append(request.GET['cholestoral'])
    lis.append(request.GET['bloodsugar'])
    lis.append(request.GET['restecg'])
    lis.append(request.GET['maximum heart rate achieved'])
    lis.append(request.GET['exercise induced angina'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['ca'])
    lis.append(request.GET['thal'])
    lis.append(request.GET['slope'])

    ans=lr.predict([lis])

    return render(request,'result_heart.html',{'ans':ans})
def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login_page.html')
    return render(request,'login_page.html')
def logout_user(request):
    logout(request)
    return redirect('/')
