from django.contrib import admin
from quiz.models import Aspect, Word, Question
# Register your models here.

class WordInline(admin.TabularInline):
    model = Word
    extra = 30

class AspectAdmin(admin.ModelAdmin):
    inlines = [WordInline]

class QuestionAdmin(admin.ModelAdmin):
    fields = ['prime', 'question', 'order']
    
    list_display = ('question', 'order')

admin.site.register(Aspect, AspectAdmin)
admin.site.register(Question, QuestionAdmin)
