from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User



def multi_role(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user is None or request.user == 'AnonymousUser':
                return HttpResponse("Please Log In")

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse("Please Log in")
        return wrapper_func
    return decorator


def user_logged_in(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return redirect('UserPage')
        else:
            return redirect('LoginPage')
    return wrapper_func
