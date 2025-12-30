from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
# model lai admin ma register gareko 
class TaskAdmin(admin.ModelAdmin):
    # customize gareko admin lai 
    list_display=('title','completed','created_at')
    list_filter=('completed','created_at')
    search_fields=('title','description')
    ordering=(' -created_at',)