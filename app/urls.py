from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include
router = DefaultRouter()
router.register('user',BotUserViewset)
router.register('test',TestViewset)
router.register('student',StudentViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('myuser/<str:t_id>/',GetUser.as_view()),
    path('olddata/<str:t_id>/<str:code>/',GetOldData.as_view()),
    path('checkstudent/<str:t_id>/<str:code>/',CheckTestStudent.as_view()),
    path('gettest/<str:code>/',GetTestAnswers.as_view()),
     path('change/<str:code>/',ChangerTestStatus.as_view()),
    path('check/<str:t_id>/',CheckUser.as_view()),
    path('update/<str:t_id>/<str:name>/<str:surname>/',UpdateBotUser.as_view()),
    path('create/<str:t_id>/<str:subject>/<str:answers>/',CreateTest.as_view())
]
