# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import User


@api_view(['GET'])
def getUser(request):
    try:
        # Assuming you want to get a user by their email, for example
        email = request.query_params.get('email')
        if not email:
            return Response({"error": "Email parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(email=email)
        user_data = {
            "ho_ten": user.ho_ten,
            "email": user.email,
            "so_dien_thoai": user.so_dien_thoai,
            "vai_tro": user.vai_tro,
            "luong": str(user.luong)  # Convert Decimal to string for JSON serialization
        }
        return Response(user_data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('mat_khau')

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
        if user.mat_khau == password:
            return Response({"message": "login successful","user_id": user.id, "user_name": user.ho_ten}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def signUp(request):
    ho_ten = request.data.get('ho_ten')
    email = request.data.get('email')
    so_dien_thoai = request.data.get('so_dien_thoai')
    mat_khau = request.data.get('mat_khau')
    vai_tro = request.data.get('vai_tro')
    luong = request.data.get('luong')

    if not all([ho_ten, email, so_dien_thoai, mat_khau, vai_tro, luong]):
        return Response({"message": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"message": "Email này đã tồn tại"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        ho_ten=ho_ten,
        email=email,
        so_dien_thoai=so_dien_thoai,
        mat_khau=mat_khau,
        vai_tro=vai_tro,
        luong=luong
    )

    return Response({"message": "đăng ký thành công", "user_id": user.id}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update(request):
    user_id = request.data.get('user_id')
    ho_ten = request.data.get('ho_ten')
    email = request.data.get('email')
    so_dien_thoai = request.data.get('so_dien_thoai')
    mat_khau = request.data.get('mat_khau')
    vai_tro = request.data.get('vai_tro')
    luong = request.data.get('luong')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.ho_ten = ho_ten if ho_ten else user.ho_ten
    user.email = email if email else user.email
    user.so_dien_thoai = so_dien_thoai if so_dien_thoai else user.so_dien_thoai
    user.mat_khau = mat_khau if mat_khau else user.mat_khau
    user.vai_tro = vai_tro if vai_tro else user.vai_tro
    user.luong = luong if luong else user.luong
    user.save()

    return Response({"message": "update successful"}, status=status.HTTP_200_OK)

