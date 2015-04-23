from django.test import TestCase
from django.core.urlresolvers import reverse

from social_service.test.factories import CategoryFactory
from social_service.models import Category


class CategoryViewsTest(TestCase):

    def test_list_of_categories(self):
        category = CategoryFactory()
        category.save()
        response = self.client.get(reverse('social_service:categories'))
        self.assertContains(response, category.name)
        self.assertContains(response, category.id)
