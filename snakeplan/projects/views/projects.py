from django.views.generic import list_detail
from snakeplan.projects.models import Project
from snakeplan.projects.models import Iteration


def index(request):
    return list_detail.object_list(
        request=request,
        queryset=Project.objects.all(),
        allow_empty=True
        )


def project_iterations(request, project_id):
    iterations = Iteration.objects.filter(project=project_id)
    project = iterations[0].project

    return list_detail.object_list(
        request=request,
        queryset=iterations,
        extra_context={'project_name': project},
        allow_empty=True
        )
