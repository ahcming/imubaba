from django.db import models
from django.contrib import admin
import django

class Work(models.Model):
    id = models.IntegerField(db_column="f_id", verbose_name="id", primary_key=True)
    content = models.CharField(db_column="f_content", verbose_name="待办内容", max_length=32)
    create = models.DateTimeField(db_column="f_create_time", verbose_name="创建时间", default=django.utils.timezone.now)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "t_work"
        verbose_name = '工作内容'  # 单数时显示内容
        verbose_name_plural = '工作内容'  # 复数时显示内容


# 待办之事
class Todo(models.Model):
    state_choice = (
        (1, '进行中'),
        (2, '因不可抗拒原因而推迟'),
        (3, '羞愧,未完成'),
        (0, '完成'),
    )

    id = models.IntegerField(db_column="f_id", primary_key=True, verbose_name="id")
    uid = models.CharField(db_column="f_uid", max_length=64, verbose_name="用户ID")
    content = models.CharField(db_column="f_content", max_length=2048, verbose_name="待办内容") # 可以是个JSON对象
    state = models.SmallIntegerField(db_column="f_state", default=1, choices=state_choice, verbose_name="待办状态")
    create_time = models.DateTimeField(db_column="f_create_time", verbose_name="创建时间", default=django.utils.timezone.now)
    update_time = models.DateTimeField(db_column="f_update_time", verbose_name="最后修改时间", default=django.utils.timezone.now)

    class Meta:
        db_table = "t_todo"
        verbose_name = '待办内容'  # 单数时显示内容
        verbose_name_plural = '待办清单'  # 复数时显示内容