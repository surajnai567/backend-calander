from .serializer import ProductSerializer
from product.models import Product
from django.http.response import JsonResponse
from rest_framework.views import APIView
import json
from category.models import CategoryModel
import staticdata


class GetAllProductApiView(APIView):
	def post(self, request):
		pass


class GetNewProductApiView(APIView):
	def post(self, request):
		# get token for access control
		token = ''
		serialize_products = []
		try:
			products = Product.objects.filter(is_new=True)
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = staticdata.CLOUDARY_BASE_URL+i['image']
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})


class GetHomePageProductApiView(APIView):
	def post(self, request):
		# get token for access control
		token = ''
		serialize_products = []
		try:
			products = Product.objects.filter(homepage=True)
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = staticdata.CLOUDARY_BASE_URL + i['image']
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})


class GetCategoryProductApiView(APIView):
	def post(self, request):
		# get token for access control
		category = json.loads(request.body.decode('utf-8'))
		cat = CategoryModel.objects.filter(categry=category['categry'])[0]
		print(cat)
		token = ''
		serialize_products = []
		try:
			products = Product.objects.filter(category=cat.id)
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = staticdata.CLOUDARY_BASE_URL + i['image']
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})


class GetSearchProductApiView(APIView):
	def get(self, request):
		# get token for access control
		query_string = request.GET.get('s')
		token = ''
		serialize_products = ''
		try:
			products = Product.objects.all()
			serialize_products = ProductSerializer(products, many=True).data
			for i in serialize_products:
				i['image'] = staticdata.CLOUDARY_BASE_URL + i['image']
		except:
			pass
		return JsonResponse({"code": "200", "status": "success", "products": serialize_products})

