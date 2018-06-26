from django.conf.urls import url
from trends.views import stam, keywords_collection, keyword_element

urlpatterns = [
    url(r'^api/v1/keywords/ronen/$', stam),
    url(r'^api/v1/keywords/$', keywords_collection),
    url(r'^api/v1/keywords/(?P<pk>[0-9]+)$', keyword_element),
]