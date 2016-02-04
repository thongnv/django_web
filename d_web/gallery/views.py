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


class SlideView(LoginRequiredMixin, View):
    template_name = 'gallery/slide.html'

    def get(self, request):
        if not request.user.is_active:
            HttpResponseRedirect("/")
        return render(request, self.template_name)


class ImageView(LoginRequiredMixin, View):
    template_name = 'gallery/image.html'

    def get(self, request):
        if not request.user.is_active:
            HttpResponseRedirect("/")
        return render(request, self.template_name)
