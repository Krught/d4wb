from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/minute')
def user_login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    user_server_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if len(username) >= 4 and len(username) <= 20 and len(password) >= 8 and len(password) <= 50:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['logged_in'] = True
                request.session['username'] = user.username
                return redirect('home')
            else:
                user_server_message = "Invalid username or password"
                return redirect('login')
        
        user_server_message = "Invalid username or password"
        return render(request, 'login.html', {'user_server_message': user_server_message})
    
    else:
        user_server_message = request.session.pop('server_message', "")
        return render(request, 'login.html', {'user_server_message': user_server_message})
