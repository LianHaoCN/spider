# _¡Á_ coding:utf-8 _*_  
from rest_framework import serializers
from spider.models import *
from django.contrib.auth.models import Group,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')
        
class SpiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spider
        fields = ('id','name','deep','parser_threads','fetch_threads','save_threads','max_parser_queue','max_fetch_queue','max_save_queue')