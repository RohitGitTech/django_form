# app_name/views.py
import requests
from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            api_url = "http://127.0.0.1:8000/api/register/"
            payload = {
                "email": email,
                "password": password,
            }

            response = requests.post(api_url, data=payload)
            print (response.status_code)
            if response.status_code == 201:
                
                return HttpResponse('welcome user') 
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Login failed'})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
