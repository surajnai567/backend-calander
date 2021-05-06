from rest_framework.views import APIView
import json
from order.models import OrderDetail, Order
from django.http.response import JsonResponse
from .serializer import OrderDetailSerializer
from user.models import User


class OrderDetailApiView(APIView):
	def post(self, request):
		post_data = json.loads(request.body.decode('utf-8'))
		serialized = ''
		orders = []
		products = []
		print(post_data['user_id'])
		try:
			orders = Order.objects.filter(user_id=post_data['user_id'])
			print(orders)
		except:
			pass

		# fetch all record in order related to orders
		for order in orders:
			temp = OrderDetail.objects.filter(order_id=order.id)
			for item in temp:
				item.status = order.status
				products.append(item)

		print(products)
		try:
			# serialize data
			serialized = OrderDetailSerializer(products, many=True).data

		except Exception as e:
			print(e)

		return JsonResponse({"code": 200, "status": "success", "orders": serialized})


class PlaceOrderApiView(APIView):
	def post(self, request):
		json_data = json.loads(request.body.decode('utf-8'))
		print(json_data)
		current_user = User.objects.filter(id=json_data['user_id'])[0]
		order = Order(user_id=current_user, address=json_data['address'],
					  area=json_data['area'], mobile=json_data['mobile'],
					  token=json_data['token'])
		order.save()
		order_items = json_data['orderitems']
		for item in order_items:
			item = OrderDetail(order_id=order, itemname=item['itemname'],
							   itemquantity=item['itemquantity'],
							   itemImage=item['itemImage'], attribute=item['attribute'],
							   currency=item['currency'], itemtotal=item['itemtotal'],
							   status=order.status, itemprice=item['itemprice'], total=item['itemtotal'])
			#order.totalamount = str(float(item.itemtotal) + float(order.totalamount))
			item.save()
		#order.save()
		products = []
		orders = []
		try:
			orders = Order.objects.filter(user_id=order.user_id)
			print(orders)
		except:
			pass

		# fetch all record in order related to orders
		for order in orders:
			temp = OrderDetail.objects.filter(order_id=order.id)
			for item in temp:
				products.append(item)

		print(products)
		try:
			# serialize data
			serialized = OrderDetailSerializer(products, many=True).data

		except Exception as e:
			print(e)

		return JsonResponse({"code": 200, "status": "success", "orders": serialized})


