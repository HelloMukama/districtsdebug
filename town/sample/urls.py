from django.urls import path

from . import views


urlpatterns = [
    # api/towns/
    path("districts/", views.DistrictListViewSet.as_view()),  # list  [GET]
    path("towns/", views.TownsListViewSet.as_view()),  # list  [GET]

]

