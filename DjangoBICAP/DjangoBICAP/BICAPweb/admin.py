from django.contrib import admin
from .models import *

admin.site.register(Utente)
admin.site.register(Distribuzione)
admin.site.register(Indagine)
admin.site.register(Questionario)
admin.site.register(Informazione)