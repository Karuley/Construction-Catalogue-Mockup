from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User


def unauthenticated_user(views_func):
    def wrapper_func(request, *args, **kwags):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return views_func(request, *args, **kwags)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kargs)
            else:
                return HttpResponse('You do not have permission to view this page')
            
        return wrapper_func
    return decorator

"""def company_admin():
    def decorator(view_func):
        def wrapper_func(request, *args, **kargs):
            user = request.user.company
            userid = request.user.company.id
            company = Company.objects.get(pk=userid)
            print('user :', user)
            print('company :', company)
            if user == company :
                return view_func(request, *args, **kargs)
            else:
                return HttpResponse('You do not have permission to view this page')   
                    
        return wrapper_func
    return decorator"""



"""def admin_only(view_func):
    def decorator(view_func):
        def wrapper_func(request, *args, **kargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'customer':
                return redirect('customer')

            if group == 'admin':
                return view_func(request, *args, **kargs)
            
        return wrapper_func
    return decorator"""