from django.shortcuts import render
import pyautogui


# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'loginpage.html')
        else:
            pyautogui.alert("Wrong Username or Password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def loggedin(request):
    return render(request, 'loginpage.html')
