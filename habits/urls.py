from django.urls import path
from rest_framework.routers import SimpleRouter
from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicHabitsListAPIView

app_name = HabitsConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [path("public/", PublicHabitsListAPIView.as_view(), name="public")]

urlpatterns += router.urls
