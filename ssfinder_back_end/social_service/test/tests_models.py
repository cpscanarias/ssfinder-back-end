from django.test import TestCase

from social_service.test.factories import CategoryFactory
from social_service.models import Category


class CategoryModelTest(TestCase):

	def test_category_creation(self):
		category = CategoryFactory()
		self.assertTrue(isinstance(category, Category))
