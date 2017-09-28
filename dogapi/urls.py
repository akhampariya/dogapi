#dogapi/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .controllers import DogList, DogDetails, BreedList, BreedDetails
urlpatterns = {
    url(r'^dogs/$', DogList.as_view(), name="create"),
    url(r'^dogs/(?P<pk>[0-9]+)/$', DogDetails.as_view(), name="details"),
    url(r'^breeds/$', BreedList.as_view(), name="bcreate"),
    url(r'^breeds/(?P<pk>[0-9]+)/$', BreedDetails.as_view(), name="bdetails"),
}
urlpatterns = format_suffix_patterns(urlpatterns)
