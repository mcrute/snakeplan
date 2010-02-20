from django.views.generic import list_detail
from snakeplan.projects.models import Iteration


def index(request, project_id):
    return list_detail.object_list(
        request=request,
        queryset=Iteration.objects.filter(project=project_id).all(),
        allow_empty=True
        )
