from django.urls import path
from . import views

app_name = 'Workouts'


urlpatterns = [
    path("ajax_workout/",views.ajax_workout,name="ajax_workout"),
    path("works_view/<int:id>",views.works_view,name="works_view"),
    path("works_view/<int:id>/ajax_works_view/",views.ajax_works_view,name="ajax_works_view"),
    path("works_view/<int:id>/updatework/",views.update_workout_state,name="update-workout")
]