from rest_framework.serializers import ModelSerializer
from habits.models import Habit
from habits.validators import (
    PrizeValidator,
    ActionTimeValidator,
    ConnectedHabitsValidator,
    PleasantHabitsValidator,
    PeriodicityValidator,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            PrizeValidator(connect="connected_habit", prize="prize"),
            ActionTimeValidator(field="action_time"),
            ConnectedHabitsValidator(field="connected_habit"),
            PleasantHabitsValidator(
                is_pleasant="is_pleasant", connect="connected_habit", prize="prize"
            ),
            PeriodicityValidator(field="periodicity"),
        ]
