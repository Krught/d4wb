from django.shortcuts import render, redirect
from worldboss.models import UploadedData
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from datetime import timedelta

def record_spawn(request):
    if request.method == 'POST' and request.user.is_authenticated:
        boss_name = request.POST['boss-name']
        location = request.POST['boss-location']
        datetime = request.POST['boss-datetime']
        
        datetime_conv = parse_datetime(datetime)
        datetime_conv = timezone.make_aware(datetime_conv)

        current_time = timezone.now()
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
            datetime=datetime,
            user=request.user
        )
        new_spawn.save()
        
        return redirect('home')  # Redirect to home
    else:
        return redirect('home')  # Redirect to home
