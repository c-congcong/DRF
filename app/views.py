from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User


@csrf_exempt
def user(request):
    if request.method == "GET":
        print("GET 查询")
        return HttpResponse("GET SUCCESS")

    elif request.method == "POST":
        print("post 添加")
        return HttpResponse("POST SUCCESS")

    elif request.method == "PUT":
        print("put 修改")
        return HttpResponse("PUT SUCCESS")

    elif request.method == "DELETE":
        print("delete 删除")
        return HttpResponse("DELETE SUCCESS")


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        if user_id:
            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            return JsonResponse({
                "status": 200,
                "message": "查询单个用户成功",
                "results": user_val
            })
        else:
            user_list = User.objects.all().values("username", "password", "gender")
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })
        return JsonResponse({
            "status": 500,
            "message": "查询有误！"
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        print(username,pwd)
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            if user_obj:
                return JsonResponse({
                    "status": 201,
                    "message": "创建用户成功",
                    "results": {"username": user_obj.username, "gender": user_obj.gender}
                })
            else:
                return JsonResponse({
                    "status": 500,
                    "message": "创建用户失败",
                })
        except:
            return JsonResponse({
                "status": 501,
                "message": "参数有误",
            })

    def put(self, request, *args, **kwargs):
        print("PUT 修改")
        try:
            id = kwargs.get("pk")
            if id:
                user_obj = User.objects.filter(pk=id)[0]
                if user_obj:
                    # 修改数据库数据
                    user_obj.username = '获取前端数据'
                    return JsonResponse({
                        "status": 200,
                        "message": "修改用户成功",
                        "results": {"username": user_obj.username, "gender": user_obj.gender}
                    })
                else:
                    return JsonResponse({
                        "status": 500,
                        "message": "修改用户失败",
                    })
        except:
            return JsonResponse({
                "status": 501,
                "message": "参数有误",
            })

    def delete(self, request, *args, **kwargs):
        print("DELETE 删除")
        user_id = kwargs.get("id")  # 获取id
        if user_id:  # 删除单个
            user_values = User.objects.filter(pk=user_id).delete()
            if user_values:
                return JsonResponse({
                    "status": 200,
                    "message": "删除用户成功",
                })
        else:  # 如果用户id不存且发的是delete请求  代表是删除全部用户信息
            user_list = User.objects.all().delete()
            if user_list:
                return JsonResponse({
                    "status": 201,
                    "message": "删除用户列表成功",
                })

        return JsonResponse({
            "status": 400,
            "message": "此用户不存在，无法删除",
        })


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        print(user_id)
        if user_id:  # 查询单个
            user_values = User.objects.filter(pk=user_id).values("name", "age", "gender").first()
            if user_values:
                return Response({
                    "status": 200,
                    "message": "获取用户成功",
                    "results": user_values
                })
        else:  # 如果用户id不存且发的是get请求  代表是获取全部用户信息
            user_list = User.objects.all().values("username", "password", "gender")
            if user_list:
                return Response({
                    "status": 201,
                    "message": "获取用户列表成功",
                    "results": list(user_list)
                })

        return Response({
            "status": 400,
            "message": "获取用户不存在",
        })

    def post(self, request, *args, **kwargs):
        return Response("POST GET SUCCESS")
