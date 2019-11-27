from django.contrib import admin
from userinfo.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'create_person', 'create_time']
    list_filter = ['create_time', 'create_person__username']


admin.site.register(Quote, QuoteAdmin)
