from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from social_service.models import Category
from social_service.serializers import CategorySerializer


class CategoriesList(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, format=None):
		categories = Category.objects.all()
		serializer = CategorySerializer(categories, many=True)
		return Response(serializer.data)
