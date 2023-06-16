from django.shortcuts import render, redirect
from worldboss.models import UploadedData, UserTimezone
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from datetime import timedelta
import pytz

def record_spawn(request):
    if request.method == 'POST' and request.user.is_authenticated:
        boss_name = request.POST['boss-name']
        location = request.POST['boss-location']
        datetime = request.POST['boss-datetime']
        
        datetime_conv = parse_datetime(datetime)
        print(datetime_conv)
        #datetime_conv = timezone.make_aware(datetime_conv)

        # Get the user's timezone from UserTimezone model
        try:
            user_timezone = UserTimezone.objects.get(user=request.user).timezone
        except UserTimezone.DoesNotExist:
            user_timezone = 'America/New_York'  # Default timezone

        # Convert datetime to America/New_York timezone
        print(user_timezone)
        timezone_obj = pytz.timezone(user_timezone)
        datetime_conv = timezone_obj.localize(datetime_conv)
        print(datetime_conv)

        ny_timezone_obj = pytz.timezone('America/New_York')
        datetime_conv = datetime_conv.astimezone(ny_timezone_obj)
        print(datetime_conv)


        current_time = timezone.now()
        print(current_time)
        min_allowed_time = current_time - timedelta(hours=3)

        # Check if the user has already added a location within the last 3 hours
        previous_spawn = UploadedData.objects.filter(user=request.user, datetime__gte=min_allowed_time).first()
        if previous_spawn:
            return redirect('home')  # Redirect to home

        if datetime_conv > current_time + timezone.timedelta(hours=1):
            return redirect('home')  # Redirect to home

        # Create a new instance of UploadedData and save it to the database
        new_spawn = UploadedData(
            boss_name=boss_name,
            location=location,
            datetime=datetime_conv,
            user=request.user
        )
        new_spawn.save()
        
        return redirect('home')  # Redirect to home
    else:
        return redirect('home')  # Redirect to home
