from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.serializer import SuperTypeSerializer
from .models import Super
from super_types.models import SuperType
from .serializer import SuperSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def supers_list (request):

    supers_param = request.query_params.get('type')
    supers = Super.objects.all()
    if request.method == 'GET' and 'type' in request.GET:
        supers = supers.filter(super_type__type=supers_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data, status=201)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
        
@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
        super = get_object_or_404(Super, pk=pk)
        if request.method == 'GET':
            serializer = SuperSerializer(super)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = SuperSerializer(super, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            super.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)