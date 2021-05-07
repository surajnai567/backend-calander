from django.urls import path
from user.api.apiview import UserRegisterView, UserLogin, UpdateUser,ForgetPassword, UpdatePassword


urlpatterns = [
	path('register', UserRegisterView.as_view()),
	path('login', UserLogin.as_view(),),
	path('forget', ForgetPassword.as_view(),),
	path('update', UpdatePassword.as_view(),),
	path('update-user', UpdateUser.as_view(),),

]