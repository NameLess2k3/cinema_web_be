from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Phim  # Make sure to import the Phim model
from ..serializer import PhimSerializer  # You will need a serializer for the Phim model


@api_view(['GET'])
def movies(request):
    # Get the search term from the query parameters
    search_term = request.query_params.get('search', None)

    if search_term:
        # Filter movies based on the search term
        movies = Phim.objects.filter(ten_phim__icontains=search_term)
    else:
        # If no search term is provided, return all movies
        movies = Phim.objects.all()

    # Serialize the movie data
    serializer = PhimSerializer(movies, many=True)

    # Return the serialized data in the response
    return Response(serializer.data, status=status.HTTP_200_OK)
