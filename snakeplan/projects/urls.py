from django.conf.urls.defaults import *
from projects.views.iterations import *

urlpatterns = patterns('',
    ('^(.*?)/iterations/', iteration_list),
)
