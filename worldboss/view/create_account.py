from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def create_account(request):
    logged_in = request.session.get('logged_in')
    if logged_in:
        return redirect('home')
    else:
        user_server_message = ""

        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                request.session['server_message'] = 'That email or username is already used'
                return redirect('create_account')

            password = request.POST.get('password')
            password_hash = make_password(password)
            
            new_user = User(username=username, email=email, password=password_hash)
            new_user.save()

            request.session['server_message'] = "Your account has been created. Please login."
            return redirect('login')

        else:
            user_server_message = request.session.pop('server_message', "")
            context = {
                'logged_in': logged_in,
                'user_server_message': user_server_message
            }
            return render(request, 'create_account.html', context)
