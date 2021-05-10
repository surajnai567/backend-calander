from event.models import Event
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EventSerializer
from user.models import User
import json


class CreateEventApiView(APIView):
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        email = post_data.get('email')
        token = post_data.get('token')
        user = User.objects.filter(email=email, token=token).all()
        if len(user):
            image = post_data.get('image')
            des = post_data.get('description')
            start_date = post_data.get('start_date')
            end_date = post_data.get('end_date')
            is_private = post_data.get('is_private')
            location = post_data.get('location')
            capacity = post_data.get('capacity')
            title = post_data.get('title')
            event = Event(user_id = user[0],image=image, description=des, start_date=start_date,
                          end_date=end_date, is_private= is_private,
                          location=location, capacity=capacity, title=title)
            event.save()
            return JsonResponse({"code": 200, "status": "Successfull !!", "userData": "successfully created event"})

        return JsonResponse({"code": 200, "status": "UnSuccessfull !!", "userData": "wrong credentials"})


class MyEventApiView(APIView):
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        email = post_data.get('email')
        token = post_data.get('token')
        user = User.objects.filter(email=email, token=token).all()
        if len(user):
            events = Event.objects.filter(user_id=user[0]).all()
            data = EventSerializer(events, many=True).data
            return JsonResponse({"code": 200, "status": "Successful !!", "userData": data})
        return JsonResponse({"code": 200, "status": "UnSuccessful !!", "userData": "wrong credentials"})


class TodayEventApiView(APIView):
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        email = post_data.get('email')
        token = post_data.get('token')
        date = post_data.get('date')
        user = User.objects.filter(email=email, token=token).all()
        if len(user):
            events = Event.objects.filter(user_id=user[0], start_date=date).all()
            data = EventSerializer(events, many=True).data
            return JsonResponse({"code": 200, "status": "Successful !!", "userData": data})
        return JsonResponse({"code": 200, "status": "UnSuccessful !!", "userData": "wrong credentials"})