from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(models.Note, NotesAdmin)