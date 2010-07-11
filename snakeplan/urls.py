# vim: set filencoding=utf8
"""
SnakePlan URL Configuration

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

from django.views import static
from django.conf.urls.defaults import patterns, include

from django.contrib import admin; admin.autodiscover()


urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'redirect_to', {'url': 'projects/' }),
    (r'^projects/', include('projects.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', static.serve, {'document_root':'templates/media'}),
)
