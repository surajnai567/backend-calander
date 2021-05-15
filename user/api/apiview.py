from user.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, FollowSerializer
import json
from utils import make_password, check_password
import random
from emailsender import EmailSender
import os
from event.models import Event


key = os.environ.get('key')
temp = {}
sender = EmailSender.instance(key)


class UserRegisterView(APIView):
	def post(self, request):
		# print(request.body.decode('utf-8'))
		post_data = json.loads(request.body.decode('utf-8'))
		data = User.objects.filter(email=post_data['email']).all()
		username = User.objects.filter(username=post_data['username']).all()

		post_data['password'] = make_password(post_data['password'].encode())
		if(len(data)):
			return JsonResponse({"code": 403, "status": "User email Already Exist"})

		if(len(username)):
			return JsonResponse({"code": 403, "status": "Username Already Exist"})


		#user = User(email=post_data['email'], fname=post_data['fname'], lname=post_data['lname'], password=make_password(post_data['password'].encode()))
		user = User(**post_data)
		user.save()
		response_data = User.objects.get(id=int(user.id))
		serialize_data = UserSerializer(response_data).data
		return JsonResponse({"code": 200, "status": "Registeration Successfull !!", "userData": serialize_data})


class UserLogin(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		password = post_data['password']
		try:
			data = User.objects.filter(email=post_data['email']).all()
		except:
			pass
		try:
			data = User.objects.filter(username=post_data['username']).all()
		except:
			pass

		if(len(data)):
			if check_password(data[0].password, password.encode()):
				serial_data = UserSerializer(data[0]).data
				return JsonResponse({'code': 200, "status": "Login Successfull !!", "userData": serial_data})
			else:
				return JsonResponse({'code': 200, "status": "wrong credential !!", "userData": {}})


			# perform login and return response
		return JsonResponse({"code": 400, "status": "Bad request wrong credential"})


class UpdateUser(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		token = post_data['token']
		user = User.objects.filter(email=post_data['email']).all()
		if len(user):
			if token == user[0].token:
				user[0].fname = post_data['fname']
				user[0].lname = post_data['lname']
				user[0].description = post_data['description']
				user[0].image = post_data['image']
				user[0].save()
				return JsonResponse({"code": 200, "status": "success", "userData": "profile updated successful"})
		return JsonResponse({"code": 200, "status": "success", "userData":  "updation failed"})


class ForgetPassword(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		email = post_data['email']
		otp = random.randint(100000, 999999)
		temp[email] = str(otp)
		sender.send(email, otp)
		return JsonResponse({"code": 200, "status": "success", "userData":"sent successful"})


class UpdatePassword(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		email = post_data['email']
		otp = post_data['otp']
		password = post_data['password']
		if temp.get(email) == otp:
			user = User.objects.filter(email=email).all()
			if len(user):
				user = user[0]
				user.password = make_password(password.encode())
				user.save()
				return JsonResponse({"code": 200, "status": "success", "userData": "password updated successful"})

		return JsonResponse({"code": 200, "status": "success", "userData": "wrong credential please try again"})

###


class Followers(APIView):
	def post(self, request, username):
		post_data = json.loads(request.body.decode('utf-8'))
		token = post_data['token']
		user = User.objects.filter(username=post_data['username'], token=token).all()
		if len(user):
			data = []
			user_data = User.objects.filter(username=username).all()
			if len(user_data):
				my_followes = user_data[0].followers
				for f in my_followes:
					data.append(User.objects.filter(id=f).all()[0])
					data = FollowSerializer(data, many=True).data
				return JsonResponse({"code": 200, "status": "success", "userData": data})
		return JsonResponse({"code": 200, "status": "success", "userData": []})


class Following(APIView):
	def post(self, request, username):
		post_data = json.loads(request.body.decode('utf-8'))
		token = post_data['token']
		user = User.objects.filter(username=post_data['username'], token=token).all()
		if len(user):
			data = []
			user_data = User.objects.filter(username=username).all()
			if len(user_data):
				my_followes = user_data[0].following
				for f in my_followes:
					data.append(User.objects.filter(id=f).all()[0])
					data = FollowSerializer(data, many=True).data
				return JsonResponse({"code": 200, "status": "success", "userData": data})
		return JsonResponse({"code": 200, "status": "success", "userData": []})


class AddFollowers(APIView):
	def post(self, request, username):
		post_data = json.loads(request.body.decode('utf-8'))
		token = post_data['token']
		user = User.objects.filter(username=post_data['username']).all()
		follow = username
		follow_user = User.objects.filter(username=follow).all()
		if len(user) and len(follow_user):
			if token == user[0].token:
				#search for follower and reply a list
				d = user[0].following
				d.append(follow_user[0].id)
				user[0].following = list(set(d))
				user[0].save()
				print("following", user[0].following)

				#add increase following of that user
				d = follow_user[0].followers
				d.append(user[0].id)
				follow_user[0].followers = list(set(d))
				follow_user[0].save()
				print("followers", follow_user[0].followers)

				#fetch follower list
				data = []
				my_following = user[0].following
				for f in my_following:
					data.append(User.objects.filter(id=f).all()[0])
				data = FollowSerializer(data, many=True).data

				return JsonResponse({"code": 200, "status": "success", "userData": data})
		return JsonResponse({"code": 200, "status": "success", "userData":"follower updating failed"})


class AddMyAttending(APIView):
	def post(self, request, event_id):
		post_data = json.loads(request.body.decode('utf-8'))
		token = post_data.get('token')
		user = User.objects.filter(username=post_data.get('username')).all()
		event = Event.objects.filter(id=event_id).all()
		if len(user) and len(event):
			if token == user[0].token:
				temp = user[0].events
				temp.append(event[0].id)
				user[0].events = list(set(temp))
				user[0].save()

				temp = event[0].attending_user
				temp.append(user[0].id)
				event[0].attending_user = list(set(temp))
				event[0].save()

				return JsonResponse(
					{"code": 200, "status": "success", "userData": "successful"})
		return JsonResponse({"code": 200, "status": "success", "userData": "event updating failed"})


def test(request):
	usr = User.objects.all()
	data = UserSerializer(usr, many=True).data
	return JsonResponse({"data":data})