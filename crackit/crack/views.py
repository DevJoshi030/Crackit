from django.shortcuts import HttpResponse, render, redirect
from .models import *
from django.contrib import messages
from django.views.generic import TemplateView

def home(request):
    return render(request, 'index.html')

def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        if len(email) < 3 or len(phone) < 10 :
            messages.error(request, 'Please fill the form correctly.')
        else:
            messages.success(
                request, 'Your message has been successfully sent.')
        contact = Contact(name=name, email=email,
                          phone_no=phone)
        contact.save()
        return redirect('/')
    return render(request, './index.html')

class RegisterTemplateView(TemplateView):
    template_name = './register.html'