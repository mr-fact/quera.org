from functools import wraps

from django.http import HttpResponseForbidden, HttpResponseNotFound

from projects.models import ProjectMembership


# noinspection PyPep8Naming
class projects_panel(object):
    def __init__(self, permissions=None):
        self.permissions = permissions

    def __call__(self, view_func):

        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            projects = ProjectMembership.objects.filter(user=request.user)
            if not projects:
                return HttpResponseNotFound('No projects found')
            request.memberships = projects
            current_project = ProjectMembership.objects.filter(user=request.user, is_current=True).first()
            if not current_project:
                current_project = ProjectMembership.objects.filter(user=request.user).first()
                current_project.is_current = True
                current_project.save()
            request.current_membership = current_project
            request.project = current_project.project


            for permission in kwargs.get('permissions', []):
                if not current_project.has_permission(permission):
                    return HttpResponseForbidden('Forbidden')
            return view_func(request, *args, **kwargs)

        return _wrapper_view
