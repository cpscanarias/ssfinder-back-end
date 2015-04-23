from django.contrib import admin
from django.conf.urls import include, url, patterns

from social_service.views import CategoriesList

admin.autodiscover()

social_service_urlpatterns = patterns('',
    url(r'^categories/$', 
        CategoriesList.as_view(), 
        name="categories"
    ),
)

urlpatterns = patterns(
    '',
    url(r'^', 
        include(social_service_urlpatterns, 
            namespace="social_service"
        )
    ),
)
