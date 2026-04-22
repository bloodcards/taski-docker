"""Admin configuration for API models."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin panel configuration for Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
