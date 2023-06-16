from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User

def change_password(request):
    logged_in = request.session.get('logged_in')
    if not logged_in:
        return redirect('main')
    else:
        if request.method == 'POST':
            # Retrieve the username and passwords from the form data
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')

            if len(new_password) >= 8 and len(new_password) <= 50:
                # Lookup the user by username
                user = User.objects.filter(username=request.session['username']).first()

                # Check if the password is correct
                if user is None or not check_password(current_password, user.password):
                    user_server_message = "Incorrect password."
                    messages.error(request, 'Incorrect password')
                    return redirect('settings')

                # Update the password
                user.password = make_password(new_password)
                user.save()
                user_server_message = "Your password has been updated"
                messages.success(request, 'Your password has been updated')
                return redirect('settings')

            return redirect('settings')
        else:
            # Handle GET request to display the password change form
            return redirect('login')
