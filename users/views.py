import random

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from users.forms import UserForm

from users.models import User


# Login functionality
def login(request):

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        print(phone_number, password)

        if phone_number and password:
            # authenticate user
            user = authenticate(
                request, phone_number=phone_number, password=password)

            if user is not None:
                # login user
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "TechiesPark| Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/login.html", context)
    else:
        context = {
            "title": "TechiesPark| Login",

        }
        return render(request, "users/login.html", context)


# signup functionality
def create(request):

    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():

                phone_number=form.cleaned_data["phone_number"]
                password=form.cleaned_data["password"]
                name=form.cleaned_data["first_name"]
                otp = random.randint(1000, 9999)
                user = User.objects.create_user(phone_number=phone_number, otp=otp, is_active=False, first_name=name, password=password)
                user.save()
                context = {
                    "phone_number": phone_number,
                    "title": "TechiesPark| Registration"
                }
                return render(request, 'users/otp.html', context=context)
                    
        else:
                context = {
                    "title": "TechiesPark| Registration",
                    "form": form,
                }
                return render(request, 'users/registration.html', context)

    else:
        form=UserForm()
        context = {
            "title": "TechiesPark| Registration",
            "form": form,
        }
    return render(request, 'users/registration.html', context)


# otp verification
def otp(request):
    otp = request.POST.get('otp')
    phone_number = request.POST.get('phone_number')

    if User.objects.filter(phone_number=phone_number).exists():
        instance = User.objects.get(phone_number=phone_number)

        if instance:

            print(instance.otp)

            if instance.otp == otp:
                instance.is_active = True
                instance.is_verified = True
                instance.save()
                context={
                    "title":"TechiesPark| Login",
                    "message":"Account created successfully, You are ready to go"
                }
                return render(request,"users/login.html",context)
                
            else:
                context = {
                    "message": "Invalid otp",
                    "error": True,
                    "phone_number": phone_number,
                    "title": "TechiesPark| Verification"

                }
                return render(request, 'users/otp.html', context=context)
    else:
        context = {
            "phone_number": phone_number,
            "message": "Invalid Phone number",
            "title": "TechiesPark| Verification",
            
        }
        return render(request, 'users/otp.html', context=context)
