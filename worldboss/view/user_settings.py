from django.shortcuts import render, redirect
from django.contrib import messages
from worldboss.models import UserTimezone
from worldboss.forms import UserSettingsForm
from django.contrib.auth.decorators import login_required

@login_required
def user_settings(request):
    user_timezone, _ = UserTimezone.objects.get_or_create(user=request.user)
    form = UserSettingsForm(request.POST or None, instance=user_timezone)
    logged_in = request.session.get('logged_in')
    if form.is_valid():
        form.save()
    user_server_message = request.session.pop('server_message', "")
    username = request.session.get('username')
    user = username.capitalize() if username else ""
    context = {
        'logged_in': logged_in,
        'user_server_message': user_server_message,
        'user': user,
        'form': form
    }
    return render(request, 'settings.html', context)

