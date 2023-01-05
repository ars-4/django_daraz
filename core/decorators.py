from django.http import HttpResponse



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
