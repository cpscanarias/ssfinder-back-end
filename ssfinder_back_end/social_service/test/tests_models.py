from django.test import TestCase

from social_service.test.factories import CategoryFactory, AACCFactory, \
    ProvinceFactory, TownFactory
from social_service.models import Category, AACC, Province, Town


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        category = CategoryFactory()
        self.assertTrue(isinstance(category, Category))


class AACCModelTest(TestCase):

    def test_aacc_creation(self):
        aacc = AACCFactory()
        self.assertTrue(isinstance(aacc, AACC))


class ProvinceModelTest(TestCase):

    def test_province_creation(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        self.assertTrue(isinstance(province, Province))


class TownModelTest(TestCase):

    def test_town_creation(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        self.assertTrue(isinstance(town, Town))
