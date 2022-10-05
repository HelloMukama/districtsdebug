from django.urls import path

from . import views


urlpatterns = [
    # api/towns/
    path("", views.DistrictListViewSet.as_view()),  # list  [GET]

]

