from django.views import static
from django.conf.urls.defaults import patterns, include

from django.contrib import admin
admin.autodiscover()

# Just get the admin stuff, don't actually do anything with it
from snakeplan.projects import admin as snakeplan_admin


urlpatterns = patterns('django.views.generic.simple',
     (r'^$', 'redirect_to', dict(url='/project/'))
)

urlpatterns += patterns('',
     (r'^admin/', include(admin.site.urls)),
     (r'^project/', include('snakeplan.projects.urls')),
     (r'^static/(?P<path>.*)$', static.serve, {'document_root':'../static'}),
)
