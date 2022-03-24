from django.contrib import admin
from . import models
# Register your models here.

#admin.site.register(models.url_table)


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(models.url_table, BookAdmin)