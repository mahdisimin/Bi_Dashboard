from django.contrib import admin
from IntegrationApp.models import SavedQuery

@admin.register(SavedQuery)
class SavedQueryAdmin(admin.ModelAdmin):
    list_display = ("id" , "title" , "slug" , "sql" , "created" , "updated")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    list_filter = ('created',)
# Register your models here.
