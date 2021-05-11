from django.urls import path
from user.api.apiview import UserRegisterView, UserLogin, \
	UpdateUser,ForgetPassword, UpdatePassword, AddFollowers,\
	MyFollowers,MyFollowing, AddMyAttending
from event.api.apiview import CreateEventApiView, MyEventApiView,\
	TodayEventApiView, AllEvents

urlpatterns = [
	path('register', UserRegisterView.as_view()),
	path('login', UserLogin.as_view(),),
	path('forget', ForgetPassword.as_view(),),
	path('update', UpdatePassword.as_view(),),
	path('update-user', UpdateUser.as_view(),),
	path('create-event', CreateEventApiView.as_view(),),
	path('my-event', MyEventApiView.as_view(),),
	path('today-event', TodayEventApiView.as_view(),),
	path('add-following', AddFollowers.as_view(),),
	path('my-follower', MyFollowers.as_view(),),
	path('my-following', MyFollowing.as_view(),),
	path('attending-event', AddMyAttending.as_view(),),
	path('all-event', AllEvents.as_view(),),

]