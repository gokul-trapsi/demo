from .views import *
from django.urls import path , include

app_name="user"

urlpatterns=[

    path("login-create/",Newuser.as_view({'post':'create'}),name='create'),
    path("login-list/",Userlist.as_view({'get':'list'}),name='login-list'),

    #for login user 
    path("login-lists/", Loginview.as_view({'get':'retrieve'}),name='login-detail'),

    path("login-update/<int:pk>/",Loginview.as_view({'put':'update'}),name='login-update'),
    path("login-partialupdate/<int:pk>/",Loginview.as_view({'put':'partialupdate'}),name='login-partialupdate'), 
    path("login-delete/<int:pk>/",Loginview.as_view({'delete':'delete'}),name='login-delete'),
    path("login-passwordreset/",LoginReset.as_view({'put':'passwordreset'}),name='login-passwordreset'),
    
  ]

