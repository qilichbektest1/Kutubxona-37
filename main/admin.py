from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

# (agar kerak bo'lsa, quyidagilarni avvalroq unregister qiling)
# admin.site.unregister(Group)
# admin.site.unregister(User)

class TalabaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'kurs', 'guruh', 'kitob_soni')
    list_display_links = ('ism',)
    list_filter = ('kurs', 'guruh',)
    list_per_page = 10
    list_editable = ('kurs', 'guruh')
    search_fields = ('ism',)
    # search_help_text - agar Django versiyangiz qo'llab-quvvatlasa ishlaydi,
    # aks holda olib tashlang
    # search_help_text = "Ism bo'yicha qidiring...."

class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'qaytargan_sana'

class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1

class MuallifAdmin(admin.ModelAdmin):
    inlines = (KitobInline,)

# Ro'yxatga olish:
admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Kutubxonachi)
admin.site.register(Kitob)
admin.site.register(Record, RecordAdmin)
admin.site.register(Muallif, MuallifAdmin)
