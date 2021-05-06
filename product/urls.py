from django.urls import path
from .api.apiviews import GetCategoryProductApiView, GetHomePageProductApiView,\
    GetNewProductApiView, GetSearchProductApiView

urlpatterns = [
    path('home/', GetHomePageProductApiView.as_view()),
    path('new/', GetNewProductApiView.as_view()),
    path('category/', GetCategoryProductApiView.as_view()),
    path('search/', GetSearchProductApiView.as_view()),
]