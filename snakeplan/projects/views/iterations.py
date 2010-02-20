from django.shortcuts import render_to_response
from snakeplan.projects.models import Project, Iteration

def iteration_list(request, project_id):
    iterations = Iteration.objects.filter(project=project_id)
    project = iterations[0].project

    return render_to_response("iterations/iteration_list.html",
                              {"project_name" : project.name,
                               "iterations" : iterations,
                              })
