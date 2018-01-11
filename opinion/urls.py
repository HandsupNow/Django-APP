from django.conf.urls import url

from . import views

urlpatterns = (
    url(regex=r'^add_one/$', view=views.add_one, name='add_one'),
    url(regex=r'^index/$', view=views.index, name='index'),
    url(regex=r'^detail/(?P<id>[0-9]+)/$', view=views.detail, name='detail'),
)

