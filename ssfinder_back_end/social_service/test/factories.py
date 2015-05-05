import factory

from social_service.models import Category, AACC, Province, Town

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
    code = factory.Sequence(lambda n: 'to%s' % n)
    name = factory.Sequence(lambda n: 'Town %s' % n)
