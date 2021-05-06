from rest_framework.serializers import ModelSerializer
from order.models import OrderDetail, Order


class OrderDetailSerializer(ModelSerializer):
	class Meta:
		model = OrderDetail
		fields = '__all__'