from django.contrib import admin
from image.models import Trade
from image.models import Purchase
from image.models import Goods


class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "thumbnail", 'quote', 'user_info', 'upload_time', "show",)
    search_fields = ("name",)
    list_filter = ("upload_time", 'quote__quote', 'user_info__username')
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Trade, ImageAdmin)
admin.site.register(Purchase, ImageAdmin)
admin.site.register(Goods, ImageAdmin)
admin.AdminSite.site_header = "Org后台管理"
