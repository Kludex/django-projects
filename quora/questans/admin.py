from django.contrib import admin

from .models import Question, Answer, QuestionGroup

class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    class Meta:
        model = Question

class QuestionGroupAdmin(admin.ModelAdmin):

    class Meta:
        model = QuestionGroup

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionGroup, QuestionGroupAdmin)
