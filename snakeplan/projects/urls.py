from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('snakeplan.projects.views',
    (r'^$', 'projects.index'),
    (r'^story/(.*)/', 'stories.index'),
    (r'^iteration/(.*)/', 'iterations.index'),
    (r'^create/', 'projects.create_project'),
    url(r'^(.*)/', 'projects.project_iterations', name='project_iterations'),
)
