from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users/login")
def index(request):
    
    context={
        "title": "TechiesPark| Home"
    }

    return render(request, "index.html",context)
