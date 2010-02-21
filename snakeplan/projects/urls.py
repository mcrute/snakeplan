from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('snakeplan.projects.views',
    (r'^$', 'projects.index'),
    (r'^projects/$', 'projects.index'),
    (r'^project/create/', 'projects.create_project'),
    (r'^project/(.*)/iterations/', 'projects.project_iterations'),
    (r'^iteration/(.*)/stories/', 'iterations.index'),
    (r'^story/(.*)/tasks/', 'stories.index'),
)
