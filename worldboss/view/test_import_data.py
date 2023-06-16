from datetime import datetime
from worldboss.models import Spawns
import pandas as pd
import pytz

# Set timezone
timezone = pytz.timezone("est")


# Clear the existing Spawns model entries
Spawns.objects.all().delete()

data = [
    {'boss_name': 'Avarice', 'datetime': '6/6/23 2:03', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Avarice', 'datetime': '6/6/23 7:56', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Avarice', 'datetime': '6/6/23 13:21', 'location': 'Fields of Desecration, Hawezar'},
    {'boss_name': 'Ashava', 'datetime': '6/6/23 19:15', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Ashava', 'datetime': '6/7/23 1:09', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Wandering Death', 'datetime': '6/7/23 6:34', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Wandering Death', 'datetime': '6/7/23 14:30', 'location': 'Fethis Wetlands, Hawezar'},
    {'boss_name': 'Wandering Death', 'datetime': '6/7/23 20:52', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Avarice', 'datetime': '6/8/23 1:46', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Avarice', 'datetime': '6/8/23 7:39', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Ashava', 'datetime': '6/8/23 13:05', 'location': 'The Crucible, Fractured Peaks'},
    {'boss_name': 'Ashava', 'datetime': '6/9/23 2:23', 'location': 'Fields of Desecration, Hawezar'},
    {'boss_name': 'Wandering Death', 'datetime': '6/9/23 8:16', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Wandering Death', 'datetime': '6/9/23 14:07', 'location': 'Fields of Desecration, Hawezar'},
    {'boss_name': 'Avarice', 'datetime': '6/9/23 19:36', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Avarice', 'datetime': '6/10/23 1:29', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Avarice', 'datetime': '6/10/23 6:54', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Ashava', 'datetime': '6/10/23 18:41', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Wandering Death', 'datetime': '6/11/23 2:05', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Wandering Death', 'datetime': '6/11/23 8:00', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Wandering Death', 'datetime': '6/11/23 13:25', 'location': 'The Crucible, Fractured Peaks'},
    {'boss_name': 'Avarice', 'datetime': '6/11/23 19:18', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Avarice', 'datetime': '6/12/23 1:12', 'location': 'Fields of Desecration, Hawezar'},
    {'boss_name': 'Ashava', 'datetime': '6/12/23 6:37', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Ashava', 'datetime': '6/12/23 12:31', 'location': 'The Crucible, Fractured Peaks'},
    {'boss_name': 'Ashava', 'datetime': '6/12/23 7:56', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Wandering Death', 'datetime': '6/13/23 1:49', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Wandering Death', 'datetime': '6/13/23 7:42', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Avarice', 'datetime': '6/13/23 13:09', 'location': 'The Crucible, Fractured Peaks'},
    {'boss_name': 'Avarice', 'datetime': '6/13/23 19:02', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Ashava', 'datetime': '6/14/23 2:27', 'location': 'Fields of Desecration, Hawezar'},
    {'boss_name': 'Ashava', 'datetime': '6/14/23 8:02', 'location': 'Seared Basin, Kehjistan'},
    {'boss_name': 'Ashava', 'datetime': '6/14/23 14:15', 'location': 'Caen Adar, Scosglen'},
    {'boss_name': 'Ashava', 'datetime': '6/14/23 20:39', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Wandering Death', 'datetime': '6/15/23 1:33', 'location': 'Fields of Desecration, Hawezar'},
    {'boss_name': 'Wandering Death', 'datetime': '6/15/23 6:58', 'location': 'Saraan Caldera, Dry Steppes'},
    {'boss_name': 'Avarice', 'datetime': '6/15/23 12:52', 'location': 'The Crucible, Fractured Peaks'}
]


for entry in data:
    dt = datetime.strptime(entry['datetime'], "%m/%d/%y %H:%M")
    #print(f"Importing data: {entry['boss_name']} - {dt} - {entry['location']}")
    Spawns.objects.create(boss_name=entry['boss_name'], datetime=dt, location=entry['location'])
