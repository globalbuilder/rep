
from django.core.exceptions import PermissionDenied

def user_is_role(user_role):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.user_type == user_role:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator

user_is_student = user_is_role('student')
user_is_supervisor = user_is_role('supervisor')
user_is_head = user_is_role('head')
