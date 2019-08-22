from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)

# # Register your models here.
# admin.site.register(Article)
