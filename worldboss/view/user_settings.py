from django.shortcuts import render, redirect
from django.contrib import messages

def user_settings(request):
    logged_in = request.session.get('logged_in')
    if logged_in:
        user_server_message = request.session.pop('server_message', "")
        username = request.session.get('username')
        user = username.capitalize() if username else ""
        context = {
            'logged_in': logged_in,
            'user_server_message': user_server_message,
            'user': user
        }
        return render(request, 'settings.html', context)
    else:
        user_server_message = "You need to be logged in to access this page."
        messages.error(request, 'You need to be logged in to access this page.')
        return redirect('homepage')
