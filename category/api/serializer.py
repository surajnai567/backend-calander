from rest_framework.serializers import ModelSerializer
from category.models import CategoryModel


class CategorySerializer(ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = '__all__'

