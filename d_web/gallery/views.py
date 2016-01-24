from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View


class IndexView(LoginRequiredMixin, View):
    template_name = 'gallery/view.html'

    def get(self, request):
        if not request.user.is_active:
            HttpResponseRedirect("/")
        return render(request, self.template_name)
