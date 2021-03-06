from django.contrib import admin
from myquora.models import Answer , Question , Category 


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_title","get_user_full_name", "created", "updated"]
    list_filter = ('updated',)
    search_fields =('question_title',)
    prepopulated_fields = {"slug": ("question_title",)}

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question_id","get_user_full_name", "created", "updated"]
    list_filter = ('updated',)
    search_fields =('question_id',)
    prepopulated_fields = {"slug": ("question_id",)}
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "updated"]
    list_filter = ('updated',)
    search_fields =('title',)
    prepopulated_fields = {"slug": ("title",)}


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ["tag_name", "created_time", "updated_time"]
#     list_filter = ('updated_time',)
#     search_fields = ("tag_name",)


    


