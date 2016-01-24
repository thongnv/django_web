from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'gallery/view.html'

    def get(self, request):
        if not request.session.get('member'):
            return HttpResponseRedirect('/')
        return render(request, self.template_name)
