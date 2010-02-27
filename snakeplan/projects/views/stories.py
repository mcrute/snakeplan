from django.views.generic import list_detail
from snakeplan.projects.models import Story
from snakeplan.projects.models import Task


def index(request, story_id):
    tasks = Task.objects.filter(story=story_id).all()

    return list_detail.object_detail(
        request=request,
        queryset=Story.objects.filter(id=story_id).all(),
        object_id=story_id,
        extra_context={'tasks': tasks},
        )
