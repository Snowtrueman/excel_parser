from django.urls import path
from .views import IndexView, ResultView

urlpatterns = [
    path("", IndexView.as_view(), name="main"),
    path("result/", ResultView.as_view(), name="result"),
]
