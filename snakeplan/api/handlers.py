from piston.handler import BaseHandler
from projects import models


class ProjectHandler(BaseHandler):

    allowed_methods = ('GET', )
    exclude = ()
    model = models.Project


class TaskHandler(BaseHandler):

    allowed_methods = ('GET', )
    exclude = ()
    model = models.Task


class ProjectStoryHandler(BaseHandler):

    allowed_methds = ('GET', )
    exclude = ()
    model = models.Project

    def read(self, request, id):
        return self.model.objects.get(id=id).stories.all()
