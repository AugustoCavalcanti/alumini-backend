from django.contrib import admin
from .models import *


@admin.register(Formando)
class FormandoAdmin(admin.ModelAdmin):
    pass

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    pass
