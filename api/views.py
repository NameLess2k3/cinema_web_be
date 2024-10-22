from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

@api_view(['GET'])
def get_user(request,pk=None):
    user= UserSerializer({'name':"pedro", "age":13})
    return Response(user.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    print(request)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)