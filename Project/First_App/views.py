from django.shortcuts import render

# Create your views here.

from First_App.models import Contact

# Create your views here.


def first(request):
    notice = ''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        obj = Contact(name=name,email=email,subject=subject,message=message)
        obj.save()
        notice = 'Add Sucsess'
    return render(request, 'index.html',{'notice':notice})



def login(request):
    return render(request, 'user_login.html')


def signin(request):
    return render(request, 'user_signup.html')

def menulist(request):
    return render (request,'menu_items.html')

def menu_1_student(request):
    return render(request,"menu_1_student.html")







#=========== Contact forms ==========

# def contact(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         subject=request.POST['subject']
#         message=request.POST['message']
#         obj = Contact(name=name,email=email,subject=subject,message=message)
#         obj.save()

#     return render(request, 'index.html')

#=========== contact forms ==========