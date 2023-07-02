from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')

def confirm_contact(request):
    if request.method == "GET":
        return redirect('info:contact')
    elif request.method == "POST":
        return redirect('info:contact')