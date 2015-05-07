from django.test import TestCase

from social_service.test.factories import CategoryFactory, AACCFactory, \
    ProvinceFactory, TownFactory, SocialServiceFactory
from social_service.models import Category, AACC, Province, Town, \
    SocialService


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


class SocialServiceModelTest(TestCase):

    def test_town_creation(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        category0 = CategoryFactory()
        category0.save()
        category1 = CategoryFactory()
        category1.save()
        social_service = SocialServiceFactory(town=town)
        social_service.save()
        social_service.categories.add(category0, category1)
        self.assertTrue(isinstance(social_service, SocialService))
