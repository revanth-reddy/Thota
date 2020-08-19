from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.slideshow_list, name="slideshow-list"),
    url(r"^add/$", views.slideshow_upload, name="slideshow-add"),
    url(r"^(?P<pk>\d+)/update/$", views.slideshow_edit, name="slideshow-update"),
    url(r"^(?P<pk>\d+)/delete/$", views.slideshow_delete, name="slideshow-delete"),
]
