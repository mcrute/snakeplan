from django.views.generic import list_detail
from snakeplan.projects.models import Task


def index(request, task_id):
    return list_detail.object_detail(
        request=request,
        queryset=Task.objects.filter(id=task_id).all(),
        object_id=task_id,
        )
