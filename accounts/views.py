import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST('first_name'),
        last_name = request.POST('last_name'),
        username = request.POST('username'),
        email = request.POST('email')
        password = request.POST('password')
        password2 = request.POST('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                print('Username is taken')
            elif User.objects.filter(email=email).exists():
                print('Email is taken')
            else:
                user = User.objects.create_user(username=username,
                                                first_name=first_name,
                                                last_name = last_name,
                                                email=email,
                                                password=password,
                                                password2=password2)

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('wrong logins')
            return redirect('/')
    else:
        return render(request,'login,html')

def logout(request):
    auth.logout(request)
    return redirect('/')