from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
class BotUserSerializer(ModelSerializer):
    date = serializers.SerializerMethodField(read_only=True)
    def get_date(self,obj):
        return obj.date
    class Meta:
        model = BotUser
        fields = ['id','t_id','name','surname','language','date']
        
class StudentSerializer(ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self,obj):
        return obj.username
    class Meta:
        model = Student
        fields = ['id','user','test','result','name']
class TestSerializer(ModelSerializer):
    test = StudentSerializer(many=True,required=False)
    name = serializers.SerializerMethodField(read_only=True)
    def get_name(self,obj):
        return obj.creator
    class Meta:
        model = Test
        fields = ['id','user','code','answers','status','test','name']
        

        