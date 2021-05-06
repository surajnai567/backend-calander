from django.urls import path
from .api.apiview import CategoryApiView

urlpatterns = [
    path('allcategory/', CategoryApiView.as_view()),
]