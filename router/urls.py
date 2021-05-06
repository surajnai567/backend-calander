from django.urls import path
from category.api.apiview import CategoryApiView
from product.api.apiviews import GetSearchProductApiView,GetCategoryProductApiView,\
	GetNewProductApiView, GetHomePageProductApiView

from order.api.apiviews import OrderDetailApiView,PlaceOrderApiView
from user.api.apiview import UserRegisterView, UserLogin, UpdateUser

from offer.api.apiviews import OfferApiView


urlpatterns = [
	path('register', UserRegisterView.as_view()),
	path('login', UserLogin.as_view(),),
	#path('allcategory', CategoryApiView.as_view()),
	#path('homepage', GetHomePageProductApiView.as_view()),
	#path('newProduct', GetNewProductApiView.as_view()),
	#path('getlist', GetCategoryProductApiView.as_view()),
	#path('orderDetails', OrderDetailApiView.as_view()),
	#path('search', GetSearchProductApiView.as_view()),
	#path('updateUser', UpdateUser.as_view()),
	#path('placeorder', PlaceOrderApiView.as_view()),
	#path('offer', OfferApiView.as_view())
]