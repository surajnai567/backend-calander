from django.urls import path
from .api.apiviews import OrderDetailApiView

urlpatterns = [
    path('', OrderDetailApiView.as_view()),
]