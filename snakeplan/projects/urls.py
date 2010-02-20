from django.conf.urls.defaults import patterns


urlpatterns = patterns('snakeplan.projects.views',
    (r'^$', 'projects.index'),
    (r'^story/(.*)/', 'stories.index'),
    (r'^iteration/(.*)/', 'iterations.index'),
    (r'^(.*)/', 'projects.project_iterations'),
)
