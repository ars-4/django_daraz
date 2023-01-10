from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.models import User



def multi_role(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user is None or request.user == 'AnonymousUser':
                return redirect('ForbiddenPage')

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return redirect("ForbiddenPage")
        return wrapper_func
    return decorator


def user_logged_in(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return redirect('HomePage')
        else:
            return redirect('LoginPage')
    return wrapper_func
