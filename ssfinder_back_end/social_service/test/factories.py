import factory

from social_service.models import Category

class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category %s' % n)
