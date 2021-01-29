from django.urls import path, register_converter,  re_path
from . import views, converters
from django.contrib import admin

register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter,'yyyy')


urlpatterns = [
    path('', views.week4),
    ## 带变量的URL
    path('<int:year>', views.year),  # 只接收整数，其他类型返回404
    path('<int:year>/<str:name>', views.name),
    

    ### 正则匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    ### 自定义过滤器
    path('<yyyy:year>', views.year),
    path('books',views.books),

]


