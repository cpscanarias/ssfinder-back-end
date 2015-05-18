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
    SocialServiceSummarySerializer


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
