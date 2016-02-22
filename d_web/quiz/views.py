from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render

# Create your views here.


class IndexView(LoginRequiredMixin, View):
    template_name = 'quiz/index.html'

    def get(self, request):
        if not request.user.is_active:
            HttpResponseRedirect("/")
        return render(request, self.template_name)