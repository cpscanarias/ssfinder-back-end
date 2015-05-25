import collections

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from social_service.models import Category, AACC, Province, Town, \
    SocialService
from social_service.serializers import CategorySerializer, AACCSerializer, \
    ProvinceSerializer, ProvinceWithoutAACCSerializer, TownSerializer, \
    TownWithoutProvinceSerializer, SocialServiceSerializer, \
    SocialServiceSummarySerializer, SocialServiceAddressSerializer


class CategoriesList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AACCsList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = AACCSerializer
    queryset = AACC.objects.all()


class ProvincesList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()


class ProvincesByAACCList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = ProvinceWithoutAACCSerializer

    def get_queryset(self):
        aacc_id = self.kwargs['id']
        aacc = AACC.objects.get(pk=aacc_id)
        return  Province.objects.filter(aacc=aacc)


class TownList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class TownByProvinceList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = TownWithoutProvinceSerializer

    def get_queryset(self):
        province_id = self.kwargs['id']
        province = Province.objects.get(pk=province_id)
        return  Town.objects.filter(province=province)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class SocialServicesList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = SocialServiceSerializer
    queryset = SocialService.objects.all()
    pagination_class = StandardResultsSetPagination


class SocialServicesSummaryList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = SocialServiceSummarySerializer
    queryset = SocialService.objects.all()
    pagination_class = StandardResultsSetPagination


class SocialServiceItem(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = SocialServiceSerializer
    queryset = SocialService.objects.all()

class SocialServicesAddressesList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = SocialServiceAddressSerializer
    queryset = SocialService.objects.all()

class SocialServicesCountView(APIView):
    """
    A view that returns the count of social services
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        social_services_count = SocialService.objects.count()
        content = {'social_services_count':social_services_count}
        return Response(content)


class SocialServicesSummarySearchList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )
    serializer_class = SocialServiceSummarySerializer
    queryset = SocialService.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        This view should return a list of social services
        filtering by words url parameters. For a user search by
        words
        """
        url_words = self.kwargs['words']
        words = url_words.split("/")[:-1]

        social_services = SocialService.objects.all()
        ss_search = {}
        
        for w in words:
            for ss in social_services:
                # Filter in the name (5 points)
                if w.lower() in ss.name.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 5
                    else:
                        ss_search[str(ss.pk)] = 5
                # Filter in the categories (2 points)
                for c in ss.categories.all():
                    if w.lower() in c.name.lower():
                        if str(ss.pk) in ss_search:
                            ss_search[str(ss.pk)] += 2
                        else:
                            ss_search[str(ss.pk)] = 2
                # Filter in the address (2 points)
                if w.lower() in ss.address.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 2
                    else:
                        ss_search[str(ss.pk)] = 2
                # Filter in the town (2 points)
                if w.lower() in ss.town.name.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 2
                    else:
                        ss_search[str(ss.pk)] = 2
                # Filter in the province (1 points)
                if w.lower() in ss.town.province.name.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 1
                    else:
                        ss_search[str(ss.pk)] = 1
                # Filter in the AACC (1 points)
                if w.lower() in ss.town.province.aacc.name.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 1
                    else:
                        ss_search[str(ss.pk)] = 1
                # Filter in the description (2 points)
                if w.lower() in ss.description.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 2
                    else:
                        ss_search[str(ss.pk)] = 2
                # Filter in the web (2 points)
                if w.lower() in ss.web.lower():
                    if str(ss.pk) in ss_search:
                        ss_search[str(ss.pk)] += 3
                    else:
                        ss_search[str(ss.pk)] = 3

        ordered_ss_search = collections.OrderedDict(sorted(ss_search.items()))
        final_ss_search = []
        for k, v in ordered_ss_search.iteritems():
            for ss in social_services:
                if str(ss.pk) == k:
                    final_ss_search.append(ss)
                    break

        return final_ss_search

