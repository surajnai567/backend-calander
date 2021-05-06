from user.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
import json
from utils import make_password, check_password


class UserRegisterView(APIView):
	def post(self, request):
		# print(request.body.decode('utf-8'))
		post_data = json.loads(request.body.decode('utf-8'))
		data = User.objects.filter(email=post_data['email']).all()
		post_data['password'] = make_password(post_data['password'].encode())
		if(len(data)):
			return JsonResponse({"code": 403, "status": "User Already Exist"})

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
		data = User.objects.filter(email=post_data['email']).all()
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
		user = User.objects.filter(token=post_data['token'])[0]
		serial = UserSerializer(user).data
		return JsonResponse({"code": 200, "status": "success", "userData": serial})