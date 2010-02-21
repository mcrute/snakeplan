from django.views import static
from django.conf.urls.defaults import patterns, include

from django.contrib import admin
admin.autodiscover()

# Just get the admin stuff, don't actually do anything with it
from snakeplan.projects import admin as snakeplan_admin


urlpatterns = patterns('django.views.generic.simple',
     (r'^$', 'redirect_to', dict(url='/p/projects/')),
     (r'^p/project/(?P<id>\d+)/$', 'redirect_to', dict(url='/p/project/%(id)s/iterations/')),
     (r'^p/iteration/(?P<id>\d+)/$', 'redirect_to', dict(url='/p/iteration/%(id)s/stories/')),
     (r'^p/story/(?P<id>\d+)/$', 'redirect_to', dict(url='/p/story/%(id)s/tasks/'))
)

urlpatterns += patterns('',
     (r'^admin/', include(admin.site.urls)),
     (r'^p/', include('projects.urls')),
     (r'^static/(?P<path>.*)$', static.serve, {'document_root':'../static'}),
)
