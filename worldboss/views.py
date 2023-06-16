from django.shortcuts import render
from worldboss.view.home import home
from worldboss.view.user_login import user_login
from worldboss.view.user_logout import user_logout
from worldboss.view.user_settings import user_settings
from worldboss.view.change_password import change_password
from worldboss.view.create_account import create_account
from worldboss.view.update_estimator import update_estimator
from worldboss.view.record_spawn import record_spawn
from worldboss.view.vote import vote
from worldboss.view.get_vote_counts import get_vote_counts

# Create your views here.
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

