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
    # 列表
    views_list = ["学习开发1", "学习开发2", "学习开发3"]
    return render(request, "two.html", {"views_list": views_list})


def three(request):
    # 时间
    import datetime
    now = datetime.datetime.now()
    return render(request, "three.html", {"time": now})


def four(request):
    # 选择定量字符后以省略号显示
    views_str = "学习开发学习开发学习开发学习开发"
    return render(request, "four.html", {"views_str": views_str})


def five(request):
    # safe 安全跳转
    views_str = "<a href='https:/www.baidu.com/'>点击跳转到百度</a>"
    return render(request, "five.html", {"views_str": views_str})


def six(request):
    # if else 标签
    views_num = 15
    return render(request, "six.html", {"num": views_num})


def seven(request):
    # for循环
    views_list = ["学习开发1", "学习开发2", "学习开发3"]
    return render(request, "seven.html", {"views_list": views_list})


def eight(request):
    # 遍历字典
    views_dict = {"name": "菜鸟教程", "age":18}
    return render(request, "eight.html", {"views_dict": views_dict})
# Create your views here.
