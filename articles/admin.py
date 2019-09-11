from django.contrib import admin
from .models import Article, StudentModel

@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)


@admin.register(StudentModel)
class StudentModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birthday', 'age',)

   
# # Register your models here.
# admin.site.register(Article)
