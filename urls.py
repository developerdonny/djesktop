from django.conf.urls.defaults import patterns, include, url

import os

# Set media path
media = os.path.join(
  os.path.dirname(__file__), 'media'
)

urlpatterns = patterns('',
      url(r'^$', 'djesktop.views.home', name='home'),
         (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': media}),
)
