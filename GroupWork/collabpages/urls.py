from operator import index
from django.urls import path
from .views import indexPageView, dueDatesPageView
from .views import IS401PageView, IS402PageView, IS403PageView, IS415PageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("duedates", dueDatesPageView, name="dueDates"),
    path("is401", IS401PageView, name="IS401"),
    path("is402", IS402PageView, name="IS402"),
    path("is403", IS403PageView, name="IS403"),
    path("is415", IS415PageView, name="IS415"),
]