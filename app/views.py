from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
class BotUserViewset(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
class TestViewset(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
class StudentViewset(ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
class UpdateBotUser(APIView):
    def get(self,request,name,surname,t_id):
        data = BotUser.objects.get(t_id=t_id)
        data.name = name
        data.surname = surname
        data.save()
        return Response('Updated data')
class CheckUser(APIView):
     def get(self,request,t_id):
        data = BotUser.objects.filter(t_id=t_id).exists()
        if data:
           return Response('True')
        else:
            return Response('False')
class CreateTest(APIView):
    def get(self,request,t_id,answers,subject):
        user = BotUser.objects.get(t_id=t_id)
        test = Test(user=user,subject=subject,answers=answers)
        test.save()
        return Response(f'{test.code}')
class GetUser(APIView):
    def get(self,request,t_id):
        user = BotUser.objects.filter(t_id=t_id)
        serializer = BotUserSerializer(user,many=True)
        return Response(serializer.data)
class CheckTestStudent(APIView):
    def get(self,request,t_id,code):
        user = Student.objects.filter(user=t_id,test=code)
        if user.exists():
            return Response('True')
        else:
            return Response('False')
class GetTestAnswers(APIView):
    def get(self,request,code):
        test = Test.objects.filter(code=code)
        serializer =TestSerializer(test,many=True)
        return Response(serializer.data)
class ChangerTestStatus(APIView):
    def get(self,request,code):
        test = Test.objects.get(code=code)
        test.status = not(test.status)
        test.save()
        return Response('Changed')
class GetOldData(APIView):
    def get(self,request,code,t_id):
        user= BotUser.objects.get(t_id=t_id)
        data = Student.objects.filter(test=code,user=user)
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)