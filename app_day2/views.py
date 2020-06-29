from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Students
from app_day2 import serializers
from app_day2.serializers import StudentsSerializer


class StudentsAPIVIew(APIView):

    def get(self, request, *args, **kwargs):

        stu_id = kwargs.get("pk")

        if stu_id:
            # 查询单个
            stu_obj = Students.objects.get(pk=stu_id)
            stu_ser = StudentsSerializer(stu_obj)
            data = stu_ser.data

            return Response({
                "status": 200,
                "msg": "查询单个成功",
                "results": data,
            })
        else:
            # 查询所有
            stu_list = Students.objects.all()
            stu_list_ser = StudentsSerializer(stu_list, many=True).data
            return Response({
                "status": 200,
                "msg": "查询所有成功",
                "results":stu_list_ser,
            })

    def post(self, request, *args, **kwargs):

        request_data = request.data

        if isinstance(request_data, dict):
            stu_ser = serializers.StudentsModelSerializer(data=request_data)
            many = False
        elif isinstance(request_data, list):
            stu_ser = serializers.StudentsModelSerializer(data=request_data, many=True)
            many = True
        else:
            return Response({
                "status": 200,
                "message": "数据格式有误",
            })

        stu_ser = serializers.StudentsModelSerializer(data=request_data, many=many)
        stu_ser.is_valid(raise_exception=True)
        stu_obj = stu_ser.save()

        return Response({
            "status": 200,
            "message": "success",
            "results": serializers.StudentsModelSerializer(stu_obj, many=many).data
        })
