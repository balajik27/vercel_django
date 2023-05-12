import django
from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import *
from . models import *
# Create your views here.

def login(request):
    if request.method == 'POST':
        uname = request.POST['User']
        pass1 = request.POST['password']
        user = auth.authenticate(username=uname,password=pass1)

        if user == None:
            messages.info(request,"invalid username/password")
            # return redirect('login')
            return render(request,'login.html')
        else:
            auth.login(request,user)
            # return redirect('login')
            return render(request,'forms.html')
    else:
        print("herllo")
        return render(request,'login.html')
    # return render(request,'login.html')


@login_required(login_url='login')
def initial(request):
    dict = {
        "box":False,
        "insertack" : False,
    }
    return render(request,'forms.html',context = dict)


@login_required(login_url='login')
def insert(request):
    if request.method == 'POST':
        texts = request.POST['text']
        if texts != '':
            obj = Text(text=texts)
            obj.save()
            dict = {
                "insertack" : True,
                "text" : texts, 
                "ack" : "submitted",
                "box":False
            }
        else:
            text_flag = True
            dict = {
                "text" : texts, 
                "ack" : "Not submitted",
                "notext" : text_flag,
                "box":False
            }
        return render(request,'forms.html',context = dict)
    return render(request,'forms.html')

@login_required(login_url='login')
def display(request):
    if request.method == 'POST':
        text_s = Text.objects.all()
        dict = {
            "texts" : text_s,
            "box":True
        }
        return render(request,'forms.html',context = dict)
@login_required(login_url='login')
def delete_all(request):
    if request.method == "POST":
        text_s = Text.objects.all()
        text_s.delete()
        return redirect('/')

























# def hello(request):
#     if request.method == "POST":
#         print("casc")
#         form = Myform(request.POST)
#         if form.is_valid():
#             print("hello")
#             text = request.POST['title']
#             dict = {
#                 "form" : form,
#                 "text" : text
#             }
#             return render(request,'index.html' , context = dict)
    
#     return render(request,'index.html')