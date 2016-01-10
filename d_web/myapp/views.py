from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    context = {'message': 'Hello'}
    return render(request, "hello.html", context)


def hello1(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def bye(request):
    text = """<h1>Good bye my love!</h1>"""
    return HttpResponse(text)

# def hello(request):
#    return render(request, "myapp/template/hello.html", {})
