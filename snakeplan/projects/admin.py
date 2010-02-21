from snakeplan.projects import models
from django.contrib import admin

admin.site.register(models.Task)
admin.site.register(models.Story)
admin.site.register(models.Project)
admin.site.register(models.Iteration)
admin.site.register(models.LoggedTime)
