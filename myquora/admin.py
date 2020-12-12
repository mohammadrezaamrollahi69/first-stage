from django.contrib import admin
from myquora.models import Question , Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('question_title',) }
