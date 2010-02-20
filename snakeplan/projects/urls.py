from django.conf.urls.defaults import patterns


urlpatterns = patterns('snakeplan.projects.views',
    ('^(.*)/', 'iterations.iteration_list'),
    (r'^story/(.*)/', 'stories.index'),
)
