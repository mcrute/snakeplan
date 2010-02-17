from django.conf.urls.defaults import *
from django.contrib import admin
from snakeplan.projects import admin as snakeplan_admin

admin.autodiscover()

urlpatterns = patterns('',
    # (r'^snakeplan/', include('snakeplan.foo.urls')),
     (r'^admin/', include(admin.site.urls)),
)
