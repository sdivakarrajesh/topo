from django.urls import path
from analytics.views import AllDataView, DataByTypeView

urlpatterns = [
    path("data/", AllDataView.as_view(), name="all_data"),
    path("data/<str:file_type>/", DataByTypeView.as_view(), name="data_by_type"),
]
