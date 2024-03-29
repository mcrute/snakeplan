# vim: set filencoding=utf8
"""
SnakePlan Admin Setup

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

import models
from django.contrib.admin import ModelAdmin, site


class ProjectAdmin(ModelAdmin):

    list_display = ('name', 'active')
    ordering = ('name', )


site.register(models.Project, ProjectAdmin)
site.register(models.Iteration)
site.register(models.Story)
site.register(models.Release)
site.register(models.Feature)
site.register(models.Task)
site.register(models.Comment)
