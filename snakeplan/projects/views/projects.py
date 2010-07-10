from django.views.generic import list_detail, create_update
from django.core.urlresolvers import reverse

from snakeplan.projects.models import Project
from snakeplan.projects.models import Iteration
from snakeplan.projects.forms import ProjectForm



def index(request):
    return list_detail.object_list(
        request=request,
        queryset=Project.objects.order_by('-active', 'name').all(),
        allow_empty=True
        )


def project_iterations(request, project_id):
    project = Project.objects.get(id=project_id)
    iterations = project.iteration_set.all()

    return list_detail.object_list(
        request=request,
        queryset=iterations,
        extra_context={'project_name': project},
        allow_empty=True
        )


def create_project(request):
    post_save_redirect = '/project/%(id)s/'
    return create_update.create_object(request,
            form_class=ProjectForm,
            post_save_redirect=post_save_redirect)
