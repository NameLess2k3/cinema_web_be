from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Ve

@api_view(['POST'])
def datVe(request):
    try:
        data = request.data
        ve = Ve.objects.create(
            ngay_dat=data.get('ngay_dat'),
            tong_tien=data.get('tong_tien'),
            phuong_thuc=data.get('phuong_thuc'),
            user_id=data.get('user_id'),
            so_ghe=data.get('so_ghe'),
            lich_chieu_id=data.get('lich_chieu_id')
        )
        return Response({"message": "Đặt vé thành công", "ve_id": ve.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def thongTinVe(request, lich_chieu_id):
        ve_list = Ve.objects.filter(lich_chieu=lich_chieu_id)
        ve_data = [{
            'id': ve.id,
            'ngay_dat': ve.ngay_dat,
            'tong_tien': ve.tong_tien,
            'phuong_thuc': ve.phuong_thuc,
            'so_ghe': ve.so_ghe,
            'lich_chieu': ve.lich_chieu.id
        } for ve in ve_list]
        return Response(ve_data, status=status.HTTP_200_OK)
