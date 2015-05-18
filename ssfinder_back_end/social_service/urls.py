from django.contrib import admin
from django.conf.urls import include, url, patterns

from social_service.views import CategoriesList, AACCsList, ProvincesList, \
    ProvincesByAACCList, TownList, TownByProvinceList, SocialServicesList, \
    SocialServicesSummaryList, SocialServiceItem, \
    SocialServicesAddressesList, SocialServicesCountView

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
    url(r'^social_services/$', 
        SocialServicesList.as_view(), 
        name="social_services"
    ),
    url(r'^social_services_summary/$', 
        SocialServicesSummaryList.as_view(), 
        name="social_services_summary"
    ),
    url(r'^social_service/(?P<pk>\d+)/$', 
        SocialServiceItem.as_view(), 
        name="social_service"
    ),
    url(r'^social_services_addresses/$', 
        SocialServicesAddressesList.as_view(), 
        name="social_services_addresses"
    ),
    url(r'^social_services_count/$', 
        SocialServicesCountView.as_view(), 
        name="social_services_count"
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
