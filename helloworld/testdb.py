from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    test1 = Test(name = 'python')
    test1.save()
    return HttpResponse("<p>数据添加成功!</p>")


def getdata(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于sql中的select * from
    list = Test.objects.all()
    # # filter相当于sql中的where，可设置条件过滤结果
    # response2 = Test.objects.filter(id=2)
    # # 获取单个对象
    # response3 = Test.objects.filter(id=1)
    # # 限制返回的数据，相当于sql中的offset 0 limit 2;
    # Test.objects.order_by('name')[0:2]
    # # 数据排序
    # Test.objects.order_by('id')
    # # 上面的方法可以连锁使用
    # Test.objects.filter(name="python").order_by("id")
    # 输出所有数据
    # 初始化
    response = ""
    response1 = ""
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def update(request):
    # 修改其中一个id=1的name字段，再保存，相当于sql中的update
    test1 = Test.objects.get(id=2)
    test1.name = "Thank you"
    test1.save()
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Thank you')
    # 修改所有的列
    # Test.objects.all().update(name='Thank')
    list = Test.objects.all()
    response = ""
    response1 = ""
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
    # return HttpResponse("<p>修改成功</p>")


def delete(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse("<p>删除成功!</p>")
