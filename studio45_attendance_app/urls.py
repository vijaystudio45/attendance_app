"""studio45_attendance_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from attendance.views import login,sign_up,logout,dashboard,employee_data_add,start_data_time_add,end_data_time_add,employee_register_sec,Attendance_View

urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('employee-data-add/', employee_data_add, name='employee_data_add'),
    path('start-data-time-add/', start_data_time_add, name='start_data_time_add'),
    path('end-data-time-add/', end_data_time_add, name='end_data_time_add'),
    path('employee-register-sec/', employee_register_sec, name='employee_register_sec'),
    path('attendance-view/',  Attendance_View.as_view(), name='attendance-view'),

]
