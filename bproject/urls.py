"""bproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from accounts import views as accounts_views
from django.contrib.auth import views as dj_auth_views

urlpatterns = [
    url(r'^$', accounts_views.home, name='home'),
    url(r'^accounts/profile/$', accounts_views.home, name='cc'),
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/register/$', accounts_views.register, name='register'),
    url(r'^accounts/register/complete/$', accounts_views.registration_complete,
        name='registration_complete'),

    # url(r'^accounts/login/$', accounts_views.login, name='login'),
    url(r'^accounts/login/$', dj_auth_views.login, name='login'),
    url(r'^accounts/logout/$', dj_auth_views.logout, name='logout'),

    url(r'^accounts/close_account/$', accounts_views.close_account, name='close_account'),
]
