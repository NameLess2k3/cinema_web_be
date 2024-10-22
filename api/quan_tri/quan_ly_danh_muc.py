from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def manage_movie(request):
    # Your logic for handling movie info updates
    return Response({"message": "Movie info updated"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def manage_schedule(request):
    # Your logic for handling schedule updates
    return Response({"message": "Schedule updated"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def manage_screening_room(request):
    # Your logic for handling screening room info
    return Response({"message": "Screening room info updated"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def manage_cinema(request):
    # Your logic for handling cinema info
    return Response({"message": "Cinema info updated"}, status=status.HTTP_200_OK)

