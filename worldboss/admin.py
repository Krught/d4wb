from django.contrib import admin
from .models import Spawns, Estimated, UploadedData, UserVote, UserTimezone

# Register your models here.
class SpawnsAdmin(admin.ModelAdmin):
    list_display = ('boss_name', 'location', 'datetime')
    search_fields = ('boss_name', 'location', 'datetime')
    list_filter = ('boss_name', 'location', 'datetime')
admin.site.register(Spawns, SpawnsAdmin)


class EstimatedAdmin(admin.ModelAdmin):
    list_display = ('boss_name', 'location', 'est_datetime', 'min_datetime', 'max_datetime')
admin.site.register(Estimated, EstimatedAdmin)



class UploadedAdmin(admin.ModelAdmin):
    list_display = ('boss_name', 'location', 'datetime', 'thumbs_up', 'thumbs_down')
admin.site.register(UploadedData, UploadedAdmin)

class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'spawn', 'vote_type')
admin.site.register(UserVote, UserVoteAdmin)

class UserTimezoneAdmin(admin.ModelAdmin):
    list_display = ('user', 'timezone')
admin.site.register(UserTimezone, UserTimezoneAdmin)