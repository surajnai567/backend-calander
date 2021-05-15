from django.urls import path
from user.api.apiview import UserRegisterView, UserLogin, \
	UpdateUser,ForgetPassword, UpdatePassword, AddFollowers,\
	Followers,Following, AddMyAttending, test
from event.api.apiview import CreateEventApiView, MyEventApiView,\
	TodayEventApiView, AllEvents, event, He

urlpatterns = [
	path('register', UserRegisterView.as_view()),
	path('login', UserLogin.as_view(),),
	path('forget', ForgetPassword.as_view(),),
	path('update', UpdatePassword.as_view(),),
	path('update-user', UpdateUser.as_view(),),
	path('event', CreateEventApiView.as_view(),),
	path('event/<int:id>', event, ),
	path('event/retrieve', AllEvents.as_view(),),

	#path('my-event', MyEventApiView.as_view(),),
	#path('today-event', TodayEventApiView.as_view(),),
	#path('all-event', AllEvents.as_view(),),

	path('user/<str:username>/follow', AddFollowers.as_view(),),
	path('user/<str:username>/followers', Followers.as_view(),),
	path('user/<str:username>/following', Following.as_view(),),

	path('attending-event', AddMyAttending.as_view(),),


	path('a/<str:username>', He.as_view(),),
	path('', test,),
]