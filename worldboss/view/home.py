from django.shortcuts import render
from worldboss.models import Spawns, Estimated, UploadedData

def home(request):
    logged_in = request.session.get('logged_in')
    most_recent_spawn = Spawns.objects.latest('datetime')
    next_spawn = Estimated.objects.latest('est_datetime')
    reported_spawns = UploadedData.objects.all().order_by('-thumbs_up')

    # Change this logged in stuff
    if request.session.get('logged_in'):
        user_server_message = ""
        user_server_message = request.session.pop('server_message', "")
        all_returned_results = {
            'logged_in': logged_in,
            'user_server_message': user_server_message,
            'roster': False,
            'most_recent_spawn': most_recent_spawn,
            'next_spawn': next_spawn,
            'reported_spawns': reported_spawns
        }
        return render(request, 'homepage.html', all_returned_results)
    else:
        user_server_message = ""
        user_server_message = request.session.pop('server_message', "")
        all_returned_results = {
            'logged_in': logged_in,
            'user_server_message': user_server_message,
            'most_recent_spawn': most_recent_spawn,
            'next_spawn': next_spawn,
            'reported_spawns': reported_spawns
        }
        return render(request, 'homepage.html', all_returned_results)