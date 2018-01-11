from django.contrib import admin

from .models import OpinionBox, AnswerBox


class AnswerInline(admin.TabularInline):
    model = AnswerBox


@admin.register(OpinionBox)
class OpinionBoxAdmin(admin.ModelAdmin):
    search_fields = ['opinion_text', ]
    list_display = ['id', 'user', 'opinion_text', 'opinion_photo', 'created']
    inlines = [AnswerInline, ]






