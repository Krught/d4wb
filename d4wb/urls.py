"""d4wb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from worldboss import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('settings/', views.user_settings, name='settings'),
    path('change_password/', views.change_password, name='change_password'),
    path('create_account/', views.create_account, name='create_account'),
    path('update_estimator/', views.update_estimator, name='update_estimator'),
    path('record_spawn/', views.record_spawn, name='record_spawn'),
    path('vote/<int:id>/', views.vote, name='vote'),
    path('get_vote_counts/<int:id>/', views.get_vote_counts, name='get_vote_counts'),
    path('404/', views.page_not_found, name='404'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
