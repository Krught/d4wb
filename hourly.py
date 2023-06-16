from django.utils import timezone
import os
import django

# Set the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd4wb.settings')
django.setup()

from worldboss.models import UploadedData, Spawns

def process_uploaded_data():
    current_time = timezone.now()

    # Get all UploadedData objects
    uploaded_data = UploadedData.objects.all()

    for data in uploaded_data:
        if current_time > data.datetime:
            if data.thumbs_up >= 5 and data.thumbs_up > data.thumbs_down * 2:
                # Create a new Spawns object
                spawn = Spawns(boss_name=data.boss_name, location=data.location, datetime=data.datetime)
                spawn.save()
                print("Saved: " + str(spawn.boss_name))
            # Delete the UploadedData object
            print("Deleted: " + str(data.id))
            data.delete()
        elif data.thumbs_down > data.thumbs_up:
            # Delete the UploadedData object
            print("Deleted: " + str(data.id))
            data.delete()
process_uploaded_data()