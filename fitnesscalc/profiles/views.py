# Create your views here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('profile/profile.html', RequestContext(request))