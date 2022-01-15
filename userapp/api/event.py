from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def events(request):
    data = {'test':'test','test1':'test1'}
    return Response(data)
