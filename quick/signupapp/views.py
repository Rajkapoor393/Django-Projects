from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import pyautogui as pu


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            pu.alert("Username already exists")
            return render(request, 'b.html')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                            password=password)
            user.save()
            # print("user created")
            return redirect('/')

    else:
        return render(request, 'b.html')
