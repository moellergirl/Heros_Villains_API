from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import SuperTypeSerializer
from.models import SuperType


@api_view(['GET'])
def SuperType_list(reguest):

    appending_dict_example={}
    appending_dict_example['type']= 'Hero'
    print (appending_dict_example)

    super_types= SuperType.objects.all()
    serializer=SuperTypeSerializer(super_types,many=True)

    return Response (serializer.data)

