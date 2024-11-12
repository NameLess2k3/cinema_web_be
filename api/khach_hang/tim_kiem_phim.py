from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Phim,LichChieu,PhongChieu  # Make sure to import the Phim model
from ..serializer import PhimSerializer, LichChieuSerializer,PhongChieuSerializer  # You will need a serializer for the Phim model


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


@api_view(['GET'])
def LichChieuPhim(request):
    try:
        # Get all movie screenings
        lich_chieu_list = LichChieu.objects.select_related('phim', 'phong_chieu').all()

        # Prepare the response data
        data = []
        for lich_chieu in lich_chieu_list:
            phim_data = PhimSerializer(lich_chieu.phim).data
            phong_chieu_data = PhongChieuSerializer(lich_chieu.phong_chieu).data

            data.append({
                'id': lich_chieu.id,
                'thoi_gian': lich_chieu.thoi_gian,
                'phim': phim_data,
                'phong_chieu': phong_chieu_data,
            })

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)