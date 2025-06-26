from django.contrib import admin

# Register your models here.

from .models import Detecta, Class, DetailDetail
admin.site.register(Detecta)
admin.site.register(Class)
admin.site.register(DetailDetail)