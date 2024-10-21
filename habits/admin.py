from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "start_time", "action", "is_pleasant", "is_public")
    list_filter = ("start_time",)
