import factory

from social_service.models import Category, AACC, Province, Town, \
    SocialService

class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category %s' % n)


class AACCFactory(factory.Factory):
    class Meta:
        model = AACC

    code = factory.Sequence(lambda n: 'ac%s' % n)
    name = factory.Sequence(lambda n: 'AACC %s' % n)


class ProvinceFactory(factory.Factory):
    class Meta:
        model = Province

    aacc = factory.SubFactory(AACCFactory)
    code = factory.Sequence(lambda n: 'pr%s' % n)
    name = factory.Sequence(lambda n: 'Province %s' % n)


class TownFactory(factory.Factory):
    class Meta:
        model = Town
    
    province = factory.SubFactory(ProvinceFactory)
    name = factory.Sequence(lambda n: 'Town %s' % n)

class SocialServiceFactory(factory.Factory):
    class Meta:
        model = SocialService
    
    name = factory.Sequence(lambda n: 'Name %s' % n)
    address = factory.Sequence(lambda n: 'Address %s' % n)
    postal_code = factory.Sequence(lambda n: 'CP %s' % n)
    town = factory.SubFactory(TownFactory)
    phone = factory.Sequence(lambda n: 'Phone %s' % n)
    email = factory.Sequence(lambda n: 'email%s@ssfinder.org' % n)
    description = factory.Sequence(lambda n: 'Description %s' % n)
    web = factory.Sequence(lambda n: 'www.web%s.org' % n)
