from django.test import TestCase
from django.core.urlresolvers import reverse

from social_service.test.factories import CategoryFactory, AACCFactory, \
    ProvinceFactory, TownFactory, SocialServiceFactory


class CategoryViewsTest(TestCase):

    def test_list_of_categories(self):
        category = CategoryFactory()
        category.save()
        response = self.client.get(reverse('social_service:categories'))
        self.assertContains(response, category.name)
        self.assertContains(response, category.id)


class AACCViewsTest(TestCase):

    def test_list_of_aaccs(self):
        aacc = AACCFactory()
        aacc.save()
        response = self.client.get(reverse('social_service:aaccs'))
        self.assertContains(response, aacc.name)
        self.assertContains(response, aacc.id)
        self.assertContains(response, aacc.code)


class ProvicesViewsTest(TestCase):

    def test_list_of_provinces(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        response = self.client.get(reverse('social_service:provinces'))
        self.assertContains(response, province.name)
        self.assertContains(response, province.id)
        self.assertContains(response, province.code)
        self.assertContains(response, aacc.id)


    def test_list_of_provinces_by_aacc(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        response = self.client.get(
            reverse('social_service:provinces_by_aacc', 
                kwargs={'id': aacc.pk},
            )
        )
        self.assertContains(response, province.name)
        self.assertContains(response, province.id)
        self.assertContains(response, province.code)

class TownsViewsTest(TestCase):

    def test_list_of_towns(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        response = self.client.get(reverse('social_service:towns'))
        self.assertContains(response, town.name)
        self.assertContains(response, town.id)
        self.assertContains(response, province.id)


    def test_list_of_provinces_by_aacc(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        response = self.client.get(
            reverse('social_service:towns_by_province', 
                kwargs={'id': province.pk},
            )
        )
        self.assertContains(response, town.name)
        self.assertContains(response, town.id)


class SocialServicesViewsTest(TestCase):

    def test_list_of_social_services(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        category = CategoryFactory()
        category.save()
        social_service = SocialServiceFactory(town=town)
        social_service.save()
        social_service.categories.add(category)
        response = self.client.get(reverse('social_service:social_services'))
        self.assertContains(response, town.name)
        self.assertContains(response, town.province.name)
        self.assertContains(response, social_service.name)


    def test_list_of_social_services_sumary(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        category = CategoryFactory()
        category.save()
        social_service = SocialServiceFactory(town=town)
        social_service.save()
        social_service.categories.add(category)

        response = self.client.get(
            reverse('social_service:social_services_summary')
        )
        self.assertContains(response, town.name)
        self.assertContains(response, town.province.name)
        self.assertContains(response, social_service.name)

    def test_item_of_social_services(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        category = CategoryFactory()
        category.save()
        social_service = SocialServiceFactory(town=town)
        social_service.save()
        social_service.categories.add(category)

        response = self.client.get(
            reverse('social_service:social_service', 
                kwargs={'pk': social_service.pk},
            )
        )
        self.assertContains(response, town.name)
        self.assertContains(response, town.province.name)
        self.assertContains(response, social_service.name)

    def test_list_of_social_services_addresses(self):
        aacc = AACCFactory()
        aacc.save()
        province = ProvinceFactory(aacc=aacc)
        province.save()
        town = TownFactory(province=province)
        town.save()
        category = CategoryFactory()
        category.save()
        social_service = SocialServiceFactory(town=town)
        social_service.save()
        social_service.categories.add(category)

        response = self.client.get(
            reverse('social_service:social_services_addresses')
        )
        self.assertContains(response, town.name)
        self.assertContains(response, town.province.name)
        self.assertContains(response, social_service.name)
