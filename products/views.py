from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import requests
# Create your views here.
main_url = "https://04f0872440bcf48fb51c5f3dff957582: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@roverpartssa.myshopify.com/admin/api/2021-07/products.json"
class ProductDetail(APIView):
    def get(self, request, id, format = None):
        url = f"https://04f0872440bcf48fb51c5f3dff957582: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@roverpartssa.myshopify.com/admin/api/2021-07/products/{id}.json"
        r = requests.get(url)
        print(r.json())
        return Response(r.json())

    def post(self, request, format = None):
        print(json.loads(str(request.body, encoding = 'utf-8')))
        r = requests.post(main_url, json = json.loads(str(request.body, encoding = 'utf-8')))
        return Response(r.json())
    
    def put(self, request, id, format = None):
        url = f"https://04f0872440bcf48fb51c5f3dff957582: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@roverpartssa.myshopify.com/admin/api/2021-07/products/{id}.json"
        r = requests.put(url, json = json.loads(str(request.body, encoding = 'utf-8')))
        return Response(r.json())

    def delete(self, request, id, format = None):
        url = f"https://04f0872440bcf48fb51c5f3dff957582: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@roverpartssa.myshopify.com/admin/api/2021-07/products/{id}.json"
        r = requests.delete(url)
        return Response(r.json())

class ProductCreate(APIView):
    def post(self, request, format = None):
        print(json.loads(str(request.body, encoding = 'utf-8')))
        r = requests.post(main_url, json = json.loads(str(request.body, encoding = 'utf-8')))
        return Response(r.json())

    def get(self, request, format = None):
        r = requests.get(main_url)
        print(r.json())
        return Response(r.json())





