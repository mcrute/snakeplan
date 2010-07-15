# vim: set filencoding=utf8
"""
Story Views

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

from projects import models, forms

def create_story(request):
    return create_update.create_object(request, form_class=forms.StoryForm,
            post_save_redirect=reverse('create-story'))
