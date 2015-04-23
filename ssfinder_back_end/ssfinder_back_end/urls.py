from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^social_service/', include('social_service.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
