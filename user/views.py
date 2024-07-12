from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pasword = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not username:
            messages.info(request, 'please enter youser name')
            return render(request, 'register.html')

        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists')
            messages.info(request, 'anirudh')
            return render(request, 'register.html')

        if pasword == confirm_password:
            user = User.objects.create_user(username=username, password=pasword, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('/')
        else:

            messages.info(request, "password doesnot match")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')