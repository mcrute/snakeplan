# vim: set filencoding=utf8
"""
Project Views

@author: Mike Crute (mcrute@gmail.com)
@organization: SoftGroup Interactive, Inc.
@date: July 10, 2010
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.views.generic import list_detail, create_update
from django.core.urlresolvers import reverse

from ..models import Project, Iteration


def index(request):
    return list_detail.object_list(request,
        queryset=Project.objects.order_by('-active', 'name').all())


def project_iterations(request, project_id):
    project = Project.objects.get(id=project_id)

    return list_detail.object_list(request,
        extra_context={'project_name': project.name },
        queryset=project.iteration_set.all())


def create_project(request):
    return create_update.create_object(request, model=Project,
            post_save_redirect=reverse('project-list'))


def update_project(request, project_id):
    return create_update.update_object(request, model=Project,
            object_id=project_id,
            post_save_redirect=reverse('project-list'))
