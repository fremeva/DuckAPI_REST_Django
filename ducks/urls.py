from django.conf.urls import url
from ducks.views import DuckList

urlpatterns = [
    url('^ducks/$', DuckList.as_view(), name="listDuck"),
]