from django.urls import path
from .tai_khoan_khach_hang import signUp,login,update
from .tim_kiem_phim import movies
from .thong_tin_ve_xem_phim import thongTinVe,datVe

url_khach_hang = [
path('tai_khoan_khach_hang/signup', signUp),
path('tai_khoan_khach_hang/login', login),
path('tai_khoan_khach_hang/update', update),

path('thong_tin_ve_xem_phim/thongtinve/<int:user_id>/<int:dat_ve_id>', thongTinVe),
path('thong_tin_ve_xem_phim/thongtinve/<int:user_id>', thongTinVe),
path('thong_tin_ve_xem_phim/datve', datVe),

path('tim_kiem_phim/movies', movies)

    #path('user/<int:pk>', get_user)
]