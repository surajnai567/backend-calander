from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class UserSerializerCustom(ModelSerializer):
	class Meta:
		model = User
		fields = ['id']



class FollowSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ['fname', 'lname', 'description', 'username', 'email','image']
