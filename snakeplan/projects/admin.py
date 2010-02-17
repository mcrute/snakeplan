from snakeplan.projects import models
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Project, ProjectAdmin)


class IterationAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Iteration, IterationAdmin)


class StoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Story, StoryAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Task, TaskAdmin)


class LoggedTimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.LoggedTime, LoggedTimeAdmin)
