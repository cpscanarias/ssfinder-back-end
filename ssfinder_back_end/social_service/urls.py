from django.contrib import admin
from django.conf.urls import include, url, patterns

from social_service.views import CategoriesList, AACCsList, ProvincesList, \
    ProvincesByAACCList, TownList, TownByProvinceList

admin.autodiscover()

social_service_urlpatterns = patterns('',
    url(r'^categories/$', 
        CategoriesList.as_view(), 
        name="categories"
    ),
    url(r'^aaccs/$', 
        AACCsList.as_view(), 
        name="aaccs"
    ),
    url(r'^provinces/$', 
        ProvincesList.as_view(), 
        name="provinces"
    ),
    url(r'^provinces_by_aacc/(?P<id>\d+)/$', 
        ProvincesByAACCList.as_view(), 
        name="provinces_by_aacc"
    ),
    url(r'^towns/$', 
        TownList.as_view(), 
        name="towns"
    ),
    url(r'^towns_by_province/(?P<id>\d+)/$', 
        TownByProvinceList.as_view(), 
        name="towns_by_province"
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
