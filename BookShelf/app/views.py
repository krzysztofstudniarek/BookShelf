"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year
        },
        context_instance = RequestContext(request)
    )

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

@login_required
def shelf(request):
    return render_to_response(
    'app/shelf.html', context_instance=RequestContext(request)
    )