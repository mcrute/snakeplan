from django.db import models as m
from django.db.models import Model
from django.contrib.auth.models import User


STATUSES = (
    (0, 'Active'),
    (1, 'Inactive'),
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
    description = m.TextField(blank=True)
    active = m.BooleanField(default=True)
    hidden = m.BooleanField(default=False)
    wiki_link = m.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Iteration(Model):

    name = m.CharField(max_length=200)
    project = m.ForeignKey(Project)
    status = m.IntegerField(choices=STATUSES, default=0)
    start_date = m.DateField()
    end_date = m.DateField()
    days_worked = m.DecimalField(default=0, decimal_places=2, max_digits=5)
    description = m.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Story(Model):

    class Meta:
        verbose_name_plural = 'Stories'

    name = m.CharField(max_length=200)
    iteration = m.ForeignKey(Iteration)
    disposition = m.IntegerField(choices=DISPOSITIONS)
    customer = m.ForeignKey(User, blank=True, null=True,
                                related_name='story_customer')
    tracker = m.ForeignKey(User, blank=True, null=True)
    status = m.IntegerField(choices=STATUSES, default=0)
    priority = m.IntegerField()
    order = m.IntegerField()
    description = m.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Task(Model):

    name = m.CharField(max_length=200)
    story = m.ForeignKey(Story)
    task_type = m.IntegerField(choices=TASK_TYPES)
    disposition = m.IntegerField(choices=DISPOSITIONS)
    acceptor = m.ForeignKey(User, blank=True)
    estimated_hours = m.DecimalField(decimal_places=2, max_digits=5)
    description = m.TextField(blank=True)

    def __unicode__(self):
        return self.name


class LoggedTime(Model):

    start_time = m.DateTimeField(blank=True)
    end_time = m.DateTimeField(blank=True)
    logged_date = m.DateField()
    duration = m.DecimalField(decimal_places=2, max_digits=5)
    person1 = m.ForeignKey(User, blank=True, related_name="person1")
    person2 = m.ForeignKey(User, blank=True, related_name="person2")
    description = m.TextField(blank=True)

    def __unicode__(self):
        return self.description
