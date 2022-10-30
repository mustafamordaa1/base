from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Element
from .serializers import ElementSerializer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['POST'])

def AddElement(request):
    serializer = ElementSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)