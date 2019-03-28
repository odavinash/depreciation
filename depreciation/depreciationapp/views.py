from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  

import json
import objectpath
from django.http import JsonResponse
from collections import OrderedDict


def index(request):  
	template = loader.get_template('depreciationapp/index.html') # getting our template  
	return HttpResponse(template.render())       # rendering the template in HttpResponse  


def serchModel(request, brand):
	with open("media/json/depreciation_brand_model.json") as datafile:    
		data = json.load(datafile)
	
	model = []
	for obj in data:
		if obj['MarkaAdı'] == brand:
			model.append(obj['TipAdı'])

	model.sort()	
	return JsonResponse(model,safe=False)


def serchData(request, brand, model):
	print(brand)
	print(model)
	with open("media/json/depreciation.json") as datafile:    
		data = json.load(datafile)

	depreciation_lst = []
	
	for obj in data:
		if obj['MarkaAdı'] == brand and obj['TipAdı'] == model:
			
			for key, val in enumerate(obj):
				if key not in [0,1,2,3]:
					depreciation = {}
					depreciation[val] = obj[val];
					depreciation_lst.append(depreciation)
			break;
	
	return JsonResponse(depreciation_lst,safe=False)