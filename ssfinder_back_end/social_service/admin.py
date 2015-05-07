from django.contrib import admin

from social_service.models import Category, AACC, Province, Town, \
    SocialService


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


class AACCAdmin(admin.ModelAdmin):
    fields = ('code', 'name')

    def get_list_display(self, request):
    	return ('code', 'name')


class ProvinceAdmin(admin.ModelAdmin):
    fields = ('code', 'name', 'aacc')

    def get_list_display(self, request):
    	return ('code', 'name', 'aacc')


class TownAdmin(admin.ModelAdmin):
    fields = ('name', 'province')

    def get_list_display(self, request):
    	return ('name', 'province')


class SocialServiceAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        return ('name', 'address', 'town', 'phone', 'email')


admin.site.register(Category, CategoryAdmin)
admin.site.register(AACC, AACCAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
