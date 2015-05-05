from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import generics

from social_service.models import Category, AACC, Province, Town
from social_service.serializers import CategorySerializer, AACCSerializer, \
	ProvinceSerializer, ProvinceWithoutAACCSerializer, TownSerializer, \
	TownWithoutProvinceSerializer


class CategoriesList(generics.ListAPIView):
	renderer_classes = (JSONRenderer, )
	serializer_class = CategorySerializer

	def get_queryset(self):
		return  Category.objects.all()


class AACCsList(generics.ListAPIView):
	renderer_classes = (JSONRenderer, )
	serializer_class = AACCSerializer

	def get_queryset(self):
		return  AACC.objects.all()


class ProvincesList(generics.ListAPIView):
	renderer_classes = (JSONRenderer, )
	serializer_class = ProvinceSerializer

	def get_queryset(self):
		return  Province.objects.all()


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

	def get_queryset(self):
		return  Town.objects.all()


class TownByProvinceList(generics.ListAPIView):
	renderer_classes = (JSONRenderer, )
	serializer_class = TownWithoutProvinceSerializer

	def get_queryset(self):
		province_id = self.kwargs['id']
		province = Province.objects.get(pk=province_id)
		return  Town.objects.filter(province=province)
