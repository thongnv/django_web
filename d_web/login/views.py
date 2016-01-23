import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views import generic
from django.views.generic import View
from . forms import LoginForm
from . models import user_list

# index view (just redirect to login page)


class IndexView(View):
    template_name = 'home.html'
    form_class = LoginForm
    initial = {'key': 'value'}

    def get(self, request):
        if not request.session:
            return HttpResponseRedirect('/')
        form = self.form_class(self.initial)
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST
        for user in user_list:
            if user.email == data.get('email'):
                if user.password == data.get('password'):
                    request.session['member'] = user.name
                    return HttpResponseRedirect('/home/')

        return HttpResponse("Your username and password didn't match.")
        # return HttpResponseRedirect('/index/')


@login_required
def logged_in(request):
    return render_to_response('logged_in.html', context_instance=RequestContext(request))


class ProfileView(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/login/logged_in/')

        return render(request, self.template_name, {'form': form})
