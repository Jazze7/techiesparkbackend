from django.shortcuts import render
from users.forms import CustomerForm
from django.http import HttpResponse


def create(request):
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    else:
        form=CustomerForm()
        context={
            "form": form,

        }
        return render(request,"forms.html",context)