from django.shortcuts import render_to_response
from projects.models import Project, Iteration

def iteration_list(request, project_id):
    project = Project.objects.filter(id = project_id)
    iteration_list = Iteration.objects.filter(project = project_id)

    return render_to_response("iteration_list.html",
                              {"project_name" : project[0].name,
                               "iteration_list" : iteration_list
                              })
