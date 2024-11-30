# from django.conf.urls import url
from django.urls import re_path
from books import views


urlpatterns=[
    
    re_path(r'books/$', views.bookApi),
    re_path(r'^books/([0-9]+)$', views.bookApi),

    re_path(r'departments/$', views.departmentApi),
    re_path(r'^departments/([0-9]+)$', views.departmentApi),

]
