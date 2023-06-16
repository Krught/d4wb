from django.shortcuts import render
from worldboss.models import Spawns, Estimated, UploadedData, UserTimezone
from django.contrib.auth.models import User
from django.utils import timezone
import pytz


# def convert_to_user_timezone(datetime_value, user_timezone):
#     if datetime_value:
#         return timezone.localtime(datetime_value, pytz.timezone(user_timezone))
#     return None
def convert_to_user_timezone(datetime_value, user_timezone):
    if datetime_value:
        user_tz = pytz.timezone(user_timezone)
        localized_datetime = timezone.localtime(datetime_value, user_tz)
        return localized_datetime.replace(tzinfo=None)
    return None


def home(request):
    logged_in = request.session.get('logged_in')
    most_recent_spawn = Spawns.objects.latest('datetime')
    next_spawn = Estimated.objects.latest('est_datetime')
    reported_spawns = UploadedData.objects.all().order_by('-thumbs_up')

    # Change this logged in stuff
    if request.session.get('logged_in'):
        user_server_message = ""
        user_server_message = request.session.pop('server_message', "")
        user = User.objects.get(username=request.user.username)
        user_timezone = UserTimezone.objects.filter(user=user).values_list('timezone', flat=True).first()
        timezone_value = user_timezone or 'America/New_York'

        # Convert datetime fields to the user's timezone
        most_recent_spawn.datetime = convert_to_user_timezone(most_recent_spawn.datetime, timezone_value)

        next_spawn.est_datetime = convert_to_user_timezone(next_spawn.est_datetime, timezone_value)
        next_spawn.min_datetime = convert_to_user_timezone(next_spawn.min_datetime, timezone_value)
        next_spawn.max_datetime = convert_to_user_timezone(next_spawn.max_datetime, timezone_value)

        for spawn in reported_spawns:
            spawn.datetime = convert_to_user_timezone(spawn.datetime, timezone_value)



        all_returned_results = {
            'logged_in': logged_in,
            'user_server_message': user_server_message,
            'roster': False,
            'most_recent_spawn': most_recent_spawn,
            'next_spawn': next_spawn,
            'reported_spawns': reported_spawns,
            'user_timezone': timezone_value
        }
        return render(request, 'homepage.html', all_returned_results)
    else:
        user_server_message = ""
        user_server_message = request.session.pop('server_message', "")
        timezone_value = 'America/New_York'
        all_returned_results = {
            'logged_in': logged_in,
            'user_server_message': user_server_message,
            'most_recent_spawn': most_recent_spawn,
            'next_spawn': next_spawn,
            'reported_spawns': reported_spawns,
            'user_timezone': timezone_value
        }
        return render(request, 'homepage.html', all_returned_results)