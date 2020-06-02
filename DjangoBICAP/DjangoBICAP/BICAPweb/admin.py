from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline, NestedInlineModelAdmin


class InformazioneQuestionarioInline(NestedTabularInline):
    model = InformazioneQuestionario
    extra = 0

class InformazioneIndagineInline(NestedTabularInline):
    model = InformazioneIndagine
    extra = 0

class QuestionarioInline(NestedStackedInline):
    model = Questionario
    extra = 0
    inlines = [InformazioneQuestionarioInline]

class IndagineAdmin(NestedModelAdmin):
    inlines = [InformazioneIndagineInline, QuestionarioInline]


admin.site.register(Utente)
admin.site.register(Distribuzione)
admin.site.register(Indagine, IndagineAdmin)
admin.site.register(Questionario)
admin.site.register(InformazioneIndagine)
admin.site.register(InformazioneQuestionario)