from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline, NestedInlineModelAdmin

class AppartenenzaInline(admin.TabularInline):
    model = Utente.gruppi.through
    extra = 0

class GruppoAdmin(admin.ModelAdmin):
    inlines = [AppartenenzaInline]

class InformazioneQuestionarioInline(NestedTabularInline):
    model = InformazioneQuestionario
    extra = 0
    exclude = ('thumbnailUrl', 'tipoFile')

class InformazioneIndagineInline(NestedTabularInline):
    model = InformazioneIndagine
    extra = 0
    exclude = ('thumbnailUrl', 'tipoFile')

class QuestionarioInline(NestedStackedInline):
    model = Questionario
    extra = 0
    inlines = [InformazioneQuestionarioInline]

class IndagineAdmin(NestedModelAdmin):
    inlines = [InformazioneIndagineInline, QuestionarioInline]

    def save_model(self, request, obj, form, change):
        super(IndagineAdmin, self).save_model(request, obj, form, change)


admin.site.register(Gruppo, GruppoAdmin)
admin.site.register(Utente)
admin.site.register(Distribuzione)
admin.site.register(Indagine, IndagineAdmin)
admin.site.register(Questionario)
admin.site.register(InformazioneIndagine)
admin.site.register(InformazioneQuestionario)