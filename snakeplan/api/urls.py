# vim: set filencoding=utf8
"""
API URLConf

@author: Mike Crute (mcrute@gmail.com)
@organization: SoftGroup Interactive, Inc.
@date: July 13, 2010
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


from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource

import handlers

urlpatterns = patterns('',
    url(r'project/(?P<id>[^/]+)/stories', Resource(handlers.ProjectStoryHandler)),
    url(r'project/(?P<id>[^/]+)/', Resource(handlers.ProjectHandler)),
    url(r'project/', Resource(handlers.ProjectHandler)),

    url(r'task/(?P<id>[^/]+)/', Resource(handlers.TaskHandler)),
    url(r'task/', Resource(handlers.TaskHandler)),
)
