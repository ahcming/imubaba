from django.contrib.auth.models import User,Group
from rest_framework import serializers
from babaapi.models import Work, Todo
from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','groups')
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')

class TimestampField(serializers.Field):
    """
    This serializer field transform a datetime str to a timestamp float.
    """

    def to_representation(self, value):
        print("to_representation: %s, %s" % (value, type(value)))
        # return value.timestamp()
        return value.strftime("%Y-%m-%d %H:%M:%S")

    def to_internal_value(self, data):
        print("to_internal_value: %s, %s" % (data, type(data)))
        timestamp = float(data)
        no_tz = datetime.utcfromtimestamp(timestamp)
        return no_tz.astimezone(timezone(TIME_ZONE))

class WorkSerializer(serializers.ModelSerializer):
    # create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # create = TimestampField(source='create')

    class Meta:
        # 此处指明本序列化对应的model
        model = Work
        # fields = ('f_id', 'f_content', 'f_create_time')
        # fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # create = TimestampField(source='create_time')

    class Meta:
        # 此处指明本序列化对应的model
        model = Todo
        # fields = ('f_id', 'f_content', 'f_create_time')
        fields = '__all__'
