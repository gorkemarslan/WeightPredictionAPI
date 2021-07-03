from django.urls import path
from .views import WeightPrediction

urlpatterns = [
    path('weight/', WeightPrediction.as_view(), name='weight_prediction'),
]
