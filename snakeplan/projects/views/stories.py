from django.views.generic import list_detail
from snakeplan.projects.models import Story


def index(request, story_id):
    return list_detail.object_detail(
        request=request,
        queryset=Story.objects.filter(id=story_id).all(),
        object_id=story_id,
        )
