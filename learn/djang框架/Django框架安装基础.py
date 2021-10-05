'''
pip install django==2.2.*   安装
django-admin startproject web  启动一个项目
cd web    进入目录
python manage.py runserver     启动服务
    Performing system checks...
    System check identified no issues (0 silenced).
    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    October 05, 2021 - 15:28:46
    Django version 2.2.24, using settings 'web.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

python manage.py startapp 应用名   ：创建应用

'''

'''
创建一个应用名叫myhome
python manage.py startapp myhome 
1. 在创建的应用中，写view函数   myhome/view.py
视图函数，输出hello world
    views.py
        from django.shortcuts import render
        from django.http import HttpResponse
            def index(request):
            return HttpResponse('hello word')
2. 给当前应用指定路由        应用名/urls.py,子路由文件
    from django.contrib import admin
    from django.urls import path
    from . import views
    urlpatterns = [
        path('/', views.index),    #当访问/时就路由到view文件的index
    ]

3. 在跟路由配置当前应用   web/urls.py
    from django.contrib import admin
    from django.urls import path,include
    import myhome

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('myhome.urls'))
    ]
python manage.py runserver 重新启动服务 此时
'''