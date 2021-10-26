from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('',views.homepage,name='home-page'),
    path("register",views.register,name='register'),
    path("login",views.loginpage,name="login"),
    path("leave",views.leavepage,name="leave"),
    path("worktime",views.worktimepage,name="worktime")
]
