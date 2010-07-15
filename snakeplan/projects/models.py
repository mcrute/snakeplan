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


DAY = (
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    )

STATUSES = (
    (0, 'Draft'),
    (1, 'Started'),
    (2, 'Finished'),
    (3, 'Delivered'),
    (4, 'Accepted'),
    (5, 'Rejected'),
    )


class Project(Model):

    name = m.CharField(max_length=200)
    description = m.TextField(blank=True, null=True)
    active = m.BooleanField(default=True)
    start_date = m.DateField()

    iteration_starts = m.IntegerField(choices=DAY, default=0)
    iteration_length = m.IntegerField(default=2)
    initial_velocity = m.IntegerField(default=10)
    velocity_time_period = m.IntegerField(default=3)

    current_velocity = m.IntegerField(default=10)

    def __unicode__(self):
        return self.name


class Iteration(Model):

    project = m.ForeignKey(Project)

    name = m.CharField(max_length=200, blank=True, null=True)
    description = m.TextField(blank=True, null=True)
    start_date = m.DateField(blank=True, null=True)
    end_date = m.DateField(blank=True, null=True)

    team_strength = m.DecimalField(decimal_places=2, max_digits=1, default=1)

    def __unicode__(self):
        return self.name


class Story(Model):

    class Meta:
        verbose_name_plural = 'stories'

    project = m.ForeignKey(Project, related_name='stories')
    iteration = m.ForeignKey(Iteration, blank=True, null=True)
    tracker = m.ForeignKey(User, blank=True, null=True)
    customer = m.ForeignKey(User, blank=True, null=True,
                            related_name='story_customer')

    name = m.CharField(max_length=200)
    status = m.IntegerField(choices=STATUSES, default=0)
    accept_date = m.DateField(blank=True, null=True)
    description = m.TextField(blank=True, null=True)
    order = m.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Release(Story):

    release_date = m.DateField()


class Feature(Story):

    points = m.IntegerField(blank=True, null=True)


class Bug(Story):
    pass


class Task(Model):

    story = m.ForeignKey(Story)

    name = m.CharField(max_length=200)
    completed = m.BooleanField(default=False)
    order = m.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Comment(Model):

    user = m.ForeignKey(User)
    story = m.ForeignKey(Story)

    post_date = m.DateTimeField(auto_now=True)
    comment = m.TextField()

    def __unicode__(self):
        return self.comment
