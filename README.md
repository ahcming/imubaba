# imubaba
我是你爸爸小程序后端

## django环境搭建

安装django
> pip3 install django 

安装rest框架
> pip3 install djangorestframework

> pip3 install django-filter

> pip3 install markdown

api文档管理
> pip3 install drf-yasg

## django命令

- 创建工程
> python3 manage.py startproject imubaba

- 创建模块
> python3 manage.py startapp babaapi

- 创建超级用户
> python3 manage.py createsuperuser

- 运行服务
> python3 manage.py runserver

- 把model迁移到数据库
> python3 manage.py makemigrations
> python3 manage.py migrate

- 导出数据
> python3 manage.py dumpdata babaapi > babaapi.json

- 导入数据
> python3 manage.py loaddata babaapi.json

- 进入交互模式
> python3 manage.py shell

- 复制静态资源文件到项目目录下
> python3 manage.py collectstatic

## sqlite3操作

> sqlite3 db.sqlite3

查看db
> .databases

查看表
> .schema

查看当前配置
> .show

调整展示
> .mode column

执行sql跟mysql的一样

## [管理后台](http://127.0.0.1:8000/admin/)

## [API Django文档](http://127.0.0.1:8000/)

## [API drf文档](http://127.0.0.1:8000/docs)

## [API Swagger文档](http://127.0.0.1:8000/swagger)

## 参考资料
- [CSDN Django](https://blog.csdn.net/m0_37193944/article/details/89477424)
- [sqlite3相关命令](https://www.cnblogs.com/lone5wolf/p/10907644.html)
- [sqlite3相关命令](https://blog.csdn.net/majiakun1/article/details/41281935/)
- [django models用法](https://www.jianshu.com/p/38e0aec76e4d)
- [django orm使用](https://www.cnblogs.com/wxzhe/p/10306580.html)
