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
    exclude = ('creato_da',)

    def save_model(self, request, obj, form, change):
        obj.creato_da = request.user
        super(IndagineAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(IndagineAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creato_da=request.user)

class HideModelIndexAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser


admin.site.register(Gruppo, GruppoAdmin)
admin.site.register(Utente)
admin.site.register(Distribuzione)
admin.site.register(Indagine, IndagineAdmin)
admin.site.register(Questionario, HideModelIndexAdmin)
admin.site.register(InformazioneIndagine, HideModelIndexAdmin)
admin.site.register(InformazioneQuestionario, HideModelIndexAdmin)