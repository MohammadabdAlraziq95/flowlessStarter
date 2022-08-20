import imp
from django.contrib import admin
from fl_tags.models import Tags
from django.contrib.contenttypes.admin import GenericTabularInline
from polls.models import Choice, Question
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice

class TagsInline(GenericTabularInline):
    model = Tags

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
         TagsInline
    ]
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)