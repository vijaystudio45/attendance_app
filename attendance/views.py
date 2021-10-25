import json
#from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import User
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import signUp,loginform,employee_data_form
from studio45_attendance_app import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .import models
from middleware.auth import auth_middleware
from django.contrib.auth.hashers import make_password
# from datetime import datetime
# from datetime import timedelta
import uuid
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Employee_attendance_Model
import datetime
from datetime import date
from datetime import datetime
from django.views.generic import ListView,View
from .models import Employee_attendance_Model
from dateutil import parser



def login(request):
    url=settings.SITE_URL
    if request.method == 'POST':
        form_login = loginform(request.POST)
        if form_login.is_valid():
            email = form_login.cleaned_data['email']
            password = form_login.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['user_id'] = user.id
                try:
                    obj = Employee_attendance_Model.objects.filter(user_id=request.user.id, start_date__isnull=False,
                                                                   end_date=None, active=False).order_by('-id')[0]
                    if date.today() != obj.start_date:
                        Employee_attendance_Model.objects.filter(start_date=obj.start_date).update(active=True)
                    else:
                        pass
                except:
                    pass
                response_data = {'url': settings.SITE_URL + "dashboard/",
                                 'message': 'login Successfully',
                                 'status': 'success'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data = {'url': url, 'message': 'Invalid Details',
                                 'status': 'error'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        url = settings.SITE_URL
        form = signUp()
        form_login = loginform()
        page_title="Sign Up/Sign In"
        return render(request, 'login.html', {'form_login':form_login,'form': form, 'url': url,'page_title':page_title})

def sign_up(request):
    url = settings.SITE_URL
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                response_data = {'message': 'username already exsist',
                                 'status': 'error', 'url': url + 'signup/'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    response_data = {'message': 'email already exsist',
                                     'status': 'error', 'url': url + 'signup/'}
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                else:
                    password = form.cleaned_data['password']
                    confirm_password = form.cleaned_data['confirm_password']
                    if password != confirm_password:
                        response_data = {'message': 'password and conform password do not matched',
                                         'status': 'error', 'url': url + 'signup/'}
                        return HttpResponse(json.dumps(response_data), content_type="application/json")
                    else:
                        myuser = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                         email=email, password=password)
                        myuser.save()
                        response_data = {'message': 'Thanks for your Registration user has been created Successfully',
                                         'status': 'success', 'url': url}
        else:
            response_data = {'message': 'There is an error to submit a form please check and resubmit again',
                             'status': 'error', 'url': url}

        return HttpResponse(json.dumps(response_data), content_type="application/json")


@auth_middleware
def dashboard(request):
    url = settings.SITE_URL
    current_user = request.user.first_name
    user_first_capital=request.user.first_name[0]
    page_title = "Dashboard"
    user_email = request.user.email
    role_condition = User.objects.get(id=request.user.id)
    role = ''
    print(role_condition.role)
    if role_condition.role == 'hr':
        role = 1
    print(role)
    return render(request,'dashboard.html', {'page_title':page_title,'url': url, 'user_logged_in':current_user,'user_email':user_email,'user_first_capital':user_first_capital,'role':role})


def logout(request):
    auth_logout(request)
    messages.success(request, "Logout Successfully")
    return redirect(settings.SITE_URL)

@auth_middleware
def employee_data_add(request):
    url = settings.SITE_URL
    current_user = request.user.first_name
    user_first_capital = request.user.first_name[0]
    page_title = "Attendance"
    user_email = request.user.email
    test1=request.session.get('test1', None)

    try:
        add=Employee_attendance_Model.objects.get(user_id=request.user.id, start_date=date.today())
    except Employee_attendance_Model.DoesNotExist:
        add = None
    try:
        test2 = Employee_attendance_Model.objects.get(user_id=request.user.id, start_date=date.today(), end_date=date.today())
    except Employee_attendance_Model.DoesNotExist:
        test2 = None
    role_condition = User.objects.get(id=request.user.id)
    role = ''
    print(role_condition.role)
    if role_condition.role == 'hr':
        role = 1
    print(role)
    return render(request, 'employee_time.html',
                  {'page_title': page_title, 'url': url, 'user_logged_in': current_user, 'user_email': user_email,
                   'user_first_capital': user_first_capital,'test1':test1, 'add':add, 'test2':test2,'role':role})

def start_data_time_add(request):
    if request.is_ajax and request.method == "POST":
        Employee_attendance_Model.objects.create(user_id=request.user.id, start_date= date.today(), start_time=datetime.now().time()).save()
        request.session['test1']='read'
        response_data = {'message': 'start date time add successfully',
                         'status': 'success'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def end_data_time_add(request):
    if request.is_ajax and request.method == "POST":
        Employee_attendance_Model.objects.filter(user_id=request.user.id,start_date= date.today()).update(end_date=date.today(), end_time=datetime.now().time(), active=False)
        request.session['test1'] = None
        response_data = {'message': 'start date time add successfully',
                         'status': 'success'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def employee_register_sec(request):
    url = settings.SITE_URL
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                response_data = {'message': 'username already exsist',
                                 'status': 'error', 'url': url + 'signup/'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    response_data = {'message': 'email already exsist',
                                     'status': 'error', 'url': url + 'signup/'}
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                else:
                    password = form.cleaned_data['password']
                    confirm_password = form.cleaned_data['confirm_password']
                    if password != confirm_password:
                        response_data = {'message': 'password and conform password do not matched',
                                         'status': 'error', 'url': url + 'signup/'}
                        return HttpResponse(json.dumps(response_data), content_type="application/json")
                    else:
                        myuser = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                         email=email, password=password, role='employee')
                        myuser.save()
                        response_data = {'message': 'Thanks for your Registration user has been created Successfully',
                                         'status': 'success', 'url': url}
        else:
            response_data = {'message': 'There is an error to submit a form please check and resubmit again',
                             'status': 'error', 'url': url}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    current_user = request.user.first_name
    user_first_capital = request.user.first_name[0]
    page_title = "Employee Register"
    user_email = request.user.email
    role_condition = User.objects.get(id=request.user.id)
    role = ''
    print(role_condition.role)
    if role_condition.role == 'hr':
        role = 1
    print(role)
    form = signUp()
    url = settings.SITE_URL
    return render(request, 'employee_register.html',
                  {'page_title': page_title, 'url': url, 'user_logged_in': current_user, 'user_email': user_email,
                   'user_first_capital': user_first_capital,'role':role,'form':form})


class Attendance_View(ListView):
    model = Employee_attendance_Model
    template_name = 'view_employee_data.html'
    context_object_name = 'attendance'

    def get_queryset(self):
        filter_val = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        id = self.request.user.id
        new_context = Employee_attendance_Model.objects.filter(start_date__range=(filter_val,end_date),user_id = id)
        return new_context

    def get_context_data(self, *args, **kwargs):
        context = super(Attendance_View, self).get_context_data(**kwargs)
        context['start_date'] = self.request.GET.get('start_date')
        context['end_date']=self.request.GET.get('end_date')
        current_user = self.request.user.first_name
        user_first_capital = self.request.user.first_name[0]
        page_title = "Attendance details"
        user_email = self.request.user.email
        role_condition = User.objects.get(id=self.request.user.id)
        role = ''
        print(role_condition.role)
        if role_condition.role == 'hr':
            role = 1
        print(role)
        form = employee_data_form()
        url = settings.SITE_URL
        context['user_logged_in'] = current_user
        context['page_title'] = page_title
        context['user_email'] = user_email
        context['user_first_capital'] = user_first_capital
        context['role'] = role
        context['form'] = form
        context['url'] = url

        return context



