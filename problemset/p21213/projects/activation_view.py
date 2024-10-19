from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404

from projects.models import Project, ProjectMembership


def active_project(request, project_id):
    try:
        project = ProjectMembership.objects.get(id=project_id, user=request.user)
    except ProjectMembership.DoesNotExist:
        return HttpResponse(content='aaaaa')
    ProjectMembership.objects.filter(user=request.user, is_current=True).update(is_current=False)
    ProjectMembership.objects.filter(id=project.id).update(is_current=True)
    return redirect('index')
