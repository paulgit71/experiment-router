from django.urls import path
from .views import mturk_log

urlpatterns = [
    path("mturk/log/", mturk_log, name="mturk_log"),
]
