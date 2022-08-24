from django.urls import path
from .views import *
from django.conf.urls import url




urlpatterns=[

    path("login-create/",Newuser.as_view({'post':'create'}),name='create'),
    path("login-list/",Userlist.as_view({'get':'list'}),name='login-list'),
    path("login-lists/", Loginview.as_view({'get':'retrieve'}),name='login-detail'),
    path("login-update/<int:pk>/",Loginview.as_view({'put':'update'}),name='login-update'),
    path("login-partialupdate/<int:pk>/",Loginview.as_view({'put':'partialupdate'}),name='login-partialupdate'), 
    path("login-delete/<int:pk>/",Loginview.as_view({'delete':'delete'}),name='login-delete'),
    
  ]

