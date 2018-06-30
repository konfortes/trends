from django.conf.urls import url
from trends.views import keywords_collection, keyword_element, trends

urlpatterns = [
    url(r'^api/v1/keywords/$', keywords_collection),
    url(r'^api/v1/keywords/(?P<pk>[0-9]+)$', keyword_element),
    url(r'^api/v1/trends/$', trends),
]