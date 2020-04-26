from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(['GET'])
def callback(request):
    data = 'this is c-api response'
    return Response(json.dumps(data), status=200)
