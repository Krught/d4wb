from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    logout(request)  # Perform the logout action
    request.session['server_message'] = 'You have been logged out.'
    return redirect('home')
