# vim: set filencoding=utf8
"""
SnakePlan Accounts Models

@author: Mike Crute (mcrute@gmail.com)
@organization: SoftGroup Interactive, Inc.
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


from django.db import models as m
from django.db.models import Model
from django.contrib.auth.models import User


class UserProfile(Model):

    user = m.OneToOneField(User)

    initials = m.CharField('initials', max_length=3, blank=True)
    phone = m.CharField('phone', max_length=30, blank=True)
