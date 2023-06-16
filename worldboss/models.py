from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



# Create your models here.

class Spawns(models.Model):
    boss_name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=200)


class Estimated(models.Model):
    boss_name = models.CharField(max_length=100)
    est_datetime = models.DateTimeField()
    min_datetime = models.DateTimeField()
    max_datetime = models.DateTimeField()
    location = models.CharField(max_length=200)

class UploadedData(models.Model):
    boss_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    thumbs_up = models.PositiveIntegerField(default=0)
    thumbs_down = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spawn = models.ForeignKey(UploadedData, on_delete=models.CASCADE)
    vote_type = models.CharField(choices=(('up', 'Thumbs Up'), ('down', 'Thumbs Down')), max_length=4)

    class Meta:
        unique_together = ['user', 'spawn']




# Signal receiver function to call update_estimator
@receiver(post_save, sender=Spawns)
def handle_spawns_post_save(sender, instance, created, **kwargs):
    if created:
        from worldboss.view.update_estimator import update_estimator
        update_estimator()