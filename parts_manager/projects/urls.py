from django.conf.urls import url
from parts_manager.projects import views


app_name = 'projects'

urlpatterns = [
    url(
        r'^$',
        views.ProjectListView.as_view(),
        name='list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        views.ProjectDetailView.as_view(),
        name='detail'
    ),
]
