from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline, NestedInlineModelAdmin


class InformazioneInline(NestedTabularInline):
    model = Informazione
    extra = 0

class QuestionarioInline(NestedStackedInline):
    model = Questionario
    extra = 0
    inlines = [InformazioneInline]

class IndagineAdmin(NestedModelAdmin):
    inlines = [QuestionarioInline]


admin.site.register(Utente)
admin.site.register(Distribuzione)
admin.site.register(Indagine, IndagineAdmin)
admin.site.register(Questionario)
admin.site.register(Informazione)