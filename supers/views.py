from rest_framework.decorators import api_view
from rest_framework.response import Response
from. serializers import SuperSerializer
from.models import Super


@api_view (['GET'])
def Super_list (request):
    supers=Super.objects.all ()
    super_types_param= request.query_params.get ('super_types')
    sort_param = request.query_params.get ('sort')
    print (super_types_param)
    print (sort_param)
    serializer= SuperSerializer (supers, many=True)
    return Response (serializer.data)