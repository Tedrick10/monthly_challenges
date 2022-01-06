from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_activities_by_number),
    path("<str:month>", views.monthly_activities, name="monthly-challenges"),
]