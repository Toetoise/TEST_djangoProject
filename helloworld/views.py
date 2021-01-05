from django.shortcuts import render
from django.http import HttpResponse


def start(request):
    context = {}
    context['hello'] = '大家好 我是何同学 !'
    return render(request, 'start.html', context)
    # return HttpResponse("Hello World !")


def hello(request):
    return HttpResponse("Hello world ! ")


def one(request):
    views_name = "学习开发"
    return render(request, 'one.html', {"name": views_name})


def two(request):
    views_list = ["学习开发1", "学习开发2", "学习开发3"]
    return render(request, "two.html", {"views_list": views_list})


def three(request):
    import datetime
    now = datetime.datetime.now()
    return render(request, "three.html", {"time": now})

# Create your views here.
