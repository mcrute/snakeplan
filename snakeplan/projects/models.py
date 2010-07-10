# vim: set filencoding=utf8
"""
SnakePlan Project Models

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

from django.db import models as m
from django.db.models import Model
from django.contrib.auth.models import User


STATUSES = (
    (0, 'Draft'),
    (1, 'Defined'),
    (2, 'Estimated'),
    (3, 'Planned'),
    (4, 'Implemented'),
    (5, 'Verified'),
    (6, 'Accepted'),
    )

DISPOSITIONS = (
    (0, 'Planned'),
    (1, 'Carried Over'),
    (2, 'Added'),
    (3, 'Discovered'),
    )

TASK_TYPES = (
    (0, 'Feature'),
    (1, 'Debt'),
    (2, 'Functional Test'),
    (3, 'Acceptance Test'),
    (4, 'Overhead'),
    )


class Project(Model):

    name = m.CharField(max_length=200)
    description = m.TextField(blank=True, null=True)
    active = m.BooleanField(default=True)
    wiki_link = m.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Iteration(Model):

    project = m.ForeignKey(Project)

    name = m.CharField(max_length=200)
    description = m.TextField(blank=True, null=True)

    # It should not be possible to delete the backlog
    can_delete = m.BooleanField(default=True)

    def __unicode__(self):
        return self.name


# Not all iterations are actually open for development
# for example, the Backlog is not a development iteration.
class DevelopmentIteration(Iteration):

    active = m.BooleanField(default=True)
    start_date = m.DateField(blank=True, null=True)
    end_date = m.DateField(blank=True, null=True)


class Story(Model):

    class Meta:
        verbose_name_plural = 'Stories'

    iteration = m.ForeignKey(Iteration)
    tracker = m.ForeignKey(User, blank=True, null=True)
    customer = m.ForeignKey(User, blank=True, null=True,
                            related_name='story_customer')

    name = m.CharField(max_length=200)
    disposition = m.IntegerField(choices=DISPOSITIONS, default=0)
    status = m.IntegerField(choices=STATUSES, default=0)
    priority = m.IntegerField()
    order = m.IntegerField()
    description = m.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Task(Model):

    story = m.ForeignKey(Story)
    acceptor = m.ForeignKey(User, blank=True, null=True)

    name = m.CharField(max_length=200)
    completed = m.BooleanField(default=False)
    task_type = m.IntegerField(choices=TASK_TYPES, default=0)
    disposition = m.IntegerField(choices=DISPOSITIONS, default=0)
    estimated_hours = m.DecimalField(decimal_places=2, max_digits=5)
    description = m.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class LoggedTime(Model):

    task = m.ForeignKey(Task)
    person1 = m.ForeignKey(User, blank=True, null=True, related_name="person1")
    person2 = m.ForeignKey(User, blank=True, null=True, related_name="person2")

    logged_date = m.DateField()
    start_time = m.DateTimeField(blank=True, null=True)
    end_time = m.DateTimeField(blank=True, null=True)
    duration = m.DecimalField(decimal_places=2, max_digits=5)
    description = m.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.description
