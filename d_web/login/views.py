import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

from . forms import LoginForm


class IndexView(LoginRequiredMixin, View):
    template_name = 'home.html'
    form_class = LoginForm
    initial = {'key': 'value'}

    def get(self, request):
        """

        :type request:
        """
        if not request.user.is_active:
            return HttpResponseRedirect('/login/')
        form = self.form_class(self.initial)
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.user.is_active:
            return HttpResponseRedirect('/home/')
        request.session.set_test_cookie()
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()
                    path = request.GET.get('next')
                    if path in [None, '', u'']:
                        path = '/home/'
                    return HttpResponseRedirect(path)
                else:
                    return HttpResponse("Please enable cookies and try again.")
        return render(request, self.template_name)


def logout_view(request):
    logout(request)
    return render(request, "logout.html")


@login_required
def logged_in(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


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
