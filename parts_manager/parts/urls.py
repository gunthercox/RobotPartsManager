from django.conf.urls import url
from parts_manager.parts import views


urlpatterns = [
    url(r'^$',
        views.PartListView.as_view(),
        name='list'
    ),
    url(r'^(?P<pk>[0-9]+)/$',
        views.PartDetailView.as_view(),
        name='detail'
    ),
]
