from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from. serializers import SuperSerializer
from.models import Super


@api_view (['GET','POST'])

def Super_list (request):
    if request.method == 'GET':
        super_type_name= request.query_params.get('type')
        print(super_type_name)

        queryset=Super.objects.all()

    if super_type_name:
        queryset =  queryset.filter(super_type__type=super_type_name) 
        serializer=SuperSerializer(queryset, many=True)
        return Response (serializer.data)
    
   

    elif request.method == 'POST':
        serializer=SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data,status= status.HTTP_201_CREATED)

@api_view (['GET','PUT','DELETE'])
def supers_details(request,pk):
    supers=get_object_or_404(Super, pk=pk)
    if request.medtod == 'GET':
        serializer=SuperSerializer (supers, pk=pk)
        return Response(serializer.data)

    elif request.method == 'PUT':  
      serializer = SuperSerializer(supers, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
      
    elif request.method == 'DELETE':  
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    