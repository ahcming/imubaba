from django.shortcuts import render

from django.contrib.auth.models import User,Group
from rest_framework import viewsets,generics
from django.db import models
from babaapi.serializers import *
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import json


# 标准rest接口
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 标准rest接口
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# 标准rest接口
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# curl -vL http://127.0.0.1:8000/work?start=100
def GetWorksByRange(request):
    start = request.GET['start']
    # 从work里找id为id的数据
    work = Work.objects.values("id", "content", "create").filter(id__gt=start)
    return JsonResponse(list(work), json_dumps_params={"ensure_ascii":False}, safe=False)


# curl -vL http://127.0.0.1:8000/work/9
def GetWorkById(request, id):
    work = Work.objects.values("id", "content", "create").get(id=id)
    return JsonResponse(work, json_dumps_params={"ensure_ascii":False})


# 通过name查询, 精确匹配
def QueryWorkByName(request, name):
    works = Work.objects.values("id", "content", "create").filter(content=name)
    return JsonResponse(list(works), json_dumps_params={"ensure_ascii":False}, safe=False)


# 在content里搜索key, 模糊查询
def SearchWorkByContent(request, key):
    works = Work.objects.values("id", "content", "create").filter(content__contains=key)
    return JsonResponse(list(works), json_dumps_params={"ensure_ascii":False}, safe=False)


# 计数
def CountWork(request, start):
    c = Work.objects.values("id", "content", "create").filter(id__gt=start).count()
    return JsonResponse({'count': c}, json_dumps_params={"ensure_ascii":False}, safe=False)


# curl -vL http://127.0.0.1:8000/work/submit -d 'id=111&content=abc' -H 'X-CSRFToken: 7FLJh36nDT7MfOfMoY1aP1nHTiM2JNDoiMNXo5lCOfeGeRQr3jLMFN7Epu6VdwSi' -H 'Cookie: csrftoken=7FLJh36nDT7MfOfMoY1aP1nHTiM2JNDoiMNXo5lCOfeGeRQr3jLMFN7Epu6VdwSi; sessionid=i6zq0e350bg5johe1ls6fm7yjeg1vao7'
# 新增
def AddWork(request):
    print("request: %s \n" % request.method)
    content = request.POST.get('content')
    work = Work()
    work.content = content
    work.create = datetime.now()
    ret = work.save()
    print("work: %s" % ret)
    return JsonResponse({'code':'ok'}, json_dumps_params={"ensure_ascii":False}, safe=False)


# 更新
def UpdateWork(request):
    id = request.POST.get('id')
    content = request.POST.get('content')
    work = Work()
    work.id = id
    work.content = content
    work.create = datetime.now()
    ret = work.save()
    print("work: %s" % ret)
    return JsonResponse(work, json_dumps_params={"ensure_ascii":False}, safe=False)


# 删除
def DeleteWork(request):
    id = request.POST.get('id')
    work = Work()
    work.id = id
    ret = work.delete()
    print("work: %s" % ret)
    return JsonResponse(ret[0], json_dumps_params={"ensure_ascii":False}, safe=False)
