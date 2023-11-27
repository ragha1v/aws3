
from django.contrib import admin
from django.urls import path
from signup.views import Registration
from login.views import LogIn
from login.views import Home
from login.views import Logout
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name='home'),
    path('',Registration,name='signup'),
    path('login/',LogIn,name='login'),
    path('logout/',Logout,name='logout'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('vote/',vote,name='vote'),
    path('myadmin/',myadmin,name='myadmin'),
    path('adminlogin/',adminlogin,name='myadmin'),
    path('adminlogin/adminlogincheck',adminlogincheck,name='adminlogincheck')
    
]
