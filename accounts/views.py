from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# from django.core.context_processors import csrf
from django.template.context_processors import csrf

from accounts.forms import SignUpForm
from accounts.models import UserProfile


def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.email
            user.is_active = False
            user.save()
            UserProfile.objects.create(user=user)
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user=user)
            return render_to_response('accounts/registration_complete.html')

    else:
        form = SignUpForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('accounts/registration.html', token)


def registration_complete(request):
    return render_to_response('accounts/registration_complete.html')


@login_required()
def home(request):
    user = request.user
    if not user.is_active:
        return render_to_response('accounts/not_active.html', {'user': user})
    return render_to_response('accounts/home.html', {'user': user})


@login_required()
def close_account(request):
    user = request.user
    user.is_active = False
    user.save()
    user.profile.confirmed = False
    user.profile.closed = True
    user.profile.save()

    return render_to_response('accounts/close_account.html')
