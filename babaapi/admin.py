from django.contrib import admin
from .models import Work, Todo
from django.utils.html import format_html      #format_html是将html代码传给admin时依html格式显示，否则只显示本身字符串
# Register your models here.


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'get_create']
    search_fields = ('content','id')
    list_filter = ('content','id')
    list_editable = ['content']    #可编辑的字段，注意，默认第一个字段不可编辑，因此添加'id'为第一个字段

    list_per_page = 1

    def get_create(self, obj):
        print("create time: %s, %s" % (obj.create, type(obj.create)))
        return obj.create.strftime("%Y-%m-%d %H:%M:%S")


# 任务从进行变为完成
def finish(modelAdmin,request,queryset):
    queryset.update(state=0)
    

# 任务从进行变为延迟
def delay(modelAdmin,request,queryset):
    queryset.update(state=2)
    

# 任务从进行变为失败
def fail(modelAdmin,request,queryset):
    queryset.update(state=3)
    

# 任务进行中
def going(modelAdmin,request,queryset):
    queryset.update(state=1)
    

finish.short_description = '任务已完成'
delay.short_description = '任务已延迟'
fail.short_description = '任务已失败'
going.short_description = '任务进行中'

class TodoAdmin(admin.ModelAdmin):
    def show_state(self, obj):
        if obj.state==1:
            format_td=format_html('<span style="padding:2px;background-color:yellowgreen;color:white">进行中</span>')

        elif obj.state==2:
            format_td=format_html('<span style="padding:2px;background-color:orange;color:white">因不可抗拒原因而推迟</span>')

        elif obj.state==3:
            format_td=format_html('<span style="padding:2px;background-color:red;color:white">羞愧,未完成</span>')

        elif obj.state==0:
            format_td=format_html('<span style="padding:2px;background-color:green;color:white">完成</span>')
                
        else:
            format_td=format_html('<span style="padding:2px;background-color:blue;color:white">%s</span>' % obj.state)

        return format_td      

    def get_create_time(self, obj):
        return obj.create_time.strftime("%Y-%m-%d %H:%M:%S")
   
    def get_update_time(self, obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")


    list_display = ['id', 'uid', 'content', 'show_state', 'get_create_time', 'get_update_time']
    search_fields = ('uid', 'content')
    list_filter = ('uid', 'state')
    list_editable = ['content', 'uid']    #可编辑的字段，注意，默认第一个字段不可编辑，因此添加'id'为第一个字段
    actions = [going, finish, delay, fail]   # action中显示的选项
    
    list_per_page = 3
    show_state.short_description='状态'
    get_create_time.short_description='创建时间'
    get_update_time.short_description='更新时间'


admin.site.register(Work, WorkAdmin)
admin.site.register(Todo, TodoAdmin)
