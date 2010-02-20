from django.views.generic import list_detail
from snakeplan.projects.models import Project


def index(request):
    return list_detail.object_list(
        request=request,
        queryset=Project.objects.all(),
        allow_empty=True
        )
