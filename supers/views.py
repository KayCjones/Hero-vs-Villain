from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from super_types.models import SuperType


# Create your views here.

@api_view(['GET'])
def supers_list (request):


    return Response('ok')