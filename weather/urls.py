
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^fetch/$', views.fetch),
	url(r'^add/$', views.add),
	url(r'^addcity/$', views.add_city),
	url(r'^getcities/$', views.get_cities),
	url(r'^.*$', views.index)
]
