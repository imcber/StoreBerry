from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
	url(r'^altausuario/$', views.Alta.as_view(), name="alta"),
]