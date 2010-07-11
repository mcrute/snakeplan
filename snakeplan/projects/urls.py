# vim: set filencoding=utf8
"""
SnakePlan Project Urls

@author: Mike Crute (mcrute@gmail.com)
@date: July 09, 2010
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

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('snakeplan.projects.views',
    url(r'^$', 'projects.index', name='project-list'),

    # Projects
    url(r'^create/', 'projects.create_project', name='create-project'),
    url(r'^(\d+)/edit/', 'projects.update_project', name='edit-project'),
    url(r'^(\d+)/', 'projects.project_iterations', name='project-iterations'),

    # Iterations
    url(r'^(\d+)/iterations/(\d+)/', 'projects.index'),

    # Stories
    url(r'^(\d+)/stories/(\d+)/', 'projects.index', name='iteration-stories'),
)
