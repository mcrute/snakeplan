from django.views.generic import list_detail
from snakeplan.projects.models import Iteration

def index(request, project_id):
    iterations = Iteration.objects.filter(project=project_id)
    project = iterations[0].project

    return list_detail.object_list(
        request=request,
        template_name='iterations/iteration_list.html',
        queryset=iterations,
        extra_context={'project_name': project},
        allow_empty=True
        )
