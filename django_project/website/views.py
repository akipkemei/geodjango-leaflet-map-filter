from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from website.models import ApartmentsNY

def home(request):
	return render(request, 'website/home.html')

def info(request):
	return render(request, 'website/info.html')

@api_view(['GET'])
def get_apartments(request):
	result = ApartmentsNY.objects.all()
	data = serializers.serialize('json', result)
	return Response(data, status=status.HTTP_200_OK, content_type='application/json')

@api_view(['GET'])
def apartments_filter(request):
	request_data = request.QUERY_PARAMS
	filtered_fields = request_data['fields']

	kwargs = {}

	if "city" in filtered_fields:
		kwargs['city'] = request_data['city']
	if "price" in filtered_fields:
		price = request_data['price'] # e.g (150, 400) 
		price_values = price[1:][:-1].split(',')
		min_price = price_values[0]
		max_price = price_values[1]
		kwargs['price__range'] =  (min_price, max_price)
		print kwargs['price__range']
	if "wifi" in filtered_fields:
		kwargs['wifi'] = request_data['wifi']
	if "breakfast" in filtered_fields:
		kwargs['breakfast'] = request_data['breakfast']

	try:
		result = ApartmentsNY.objects.filter(**kwargs)
		data = serializers.serialize('json', result)
		return Response(data, status=status.HTTP_200_OK, content_type='application/json')
		
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)

