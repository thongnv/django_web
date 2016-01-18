from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views import generic
from django.views.generic import View

# index view (just redirect to login page)


class IndexView(generic.TemplateView):
    template_name = 'login.html'


# this view will run after successfully login
@login_required
def logged_in(request):
    return render_to_response('logged_in.html', context_instance=RequestContext(request))


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
