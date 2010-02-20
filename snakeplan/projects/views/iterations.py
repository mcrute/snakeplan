from django.views.generic import list_detail
from snakeplan.projects.models import Iteration
from snakeplan.projects.models import Story

def index(request, iteration_id):
    stories = Story.objects.filter(iteration=iteration_id)
    iteration = stories[0].iteration

    return list_detail.object_list(
        request=request,
        queryset=stories,
        extra_context={'iteration_name': iteration},
        allow_empty = True
        )
