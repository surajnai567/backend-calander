from django.urls import path
from user.api.apiview import UserRegisterView, UserLogin, UpdateUser,ForgetPassword, UpdatePassword
from event.api.apiview import CreateEventApiView, MyEventApiView, TodayEventApiView

urlpatterns = [
	path('register', UserRegisterView.as_view()),
	path('login', UserLogin.as_view(),),
	path('forget', ForgetPassword.as_view(),),
	path('update', UpdatePassword.as_view(),),
	path('update-user', UpdateUser.as_view(),),
	path('create-event', CreateEventApiView.as_view(),),
	path('my-event', MyEventApiView.as_view(),),
	path('today-event', TodayEventApiView.as_view(),)

]