from django.contrib.auth.models import User,Group
from rest_framework import serializers
from babaapi.models import Work, Todo

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
        return value.timestamp()

    def to_internal_value(self, data):
        timestamp = float(data)
        no_tz = datetime.utcfromtimestamp(timestamp)
        return no_tz.astimezone(timezone(TIME_ZONE))

class WorkSerializer(serializers.ModelSerializer):
    # create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # create = TimestampField(source='create')

    class Meta:
        # 此处指明本序列化对应的model
        model = Work
        # 此处指明从model对应数据表中读出哪些字段
        # id字段我们在model中并没指明应该是框架自己创建的
        # 另外我们还创建了created字段，但这里我们不加读取他，当然你要读取加上即可
        # fields = ('f_id', 'f_content', 'f_create_time')
        # fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    # create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # create = TimestampField(source='create')

    class Meta:
        # 此处指明本序列化对应的model
        model = Todo
        # 此处指明从model对应数据表中读出哪些字段
        # id字段我们在model中并没指明应该是框架自己创建的
        # 另外我们还创建了created字段，但这里我们不加读取他，当然你要读取加上即可
        # fields = ('f_id', 'f_content', 'f_create_time')
        fields = '__all__'

class ApiTodoSerializer(serializers.HyperlinkedModelSerializer):
    # create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # create = TimestampField(source='create')

    class Meta:
        # 此处指明本序列化对应的model
        model = Todo
        # 此处指明从model对应数据表中读出哪些字段
        # id字段我们在model中并没指明应该是框架自己创建的
        # 另外我们还创建了created字段，但这里我们不加读取他，当然你要读取加上即可
        # fields = ('f_id', 'f_content', 'f_create_time')
        fields = '__all__'
