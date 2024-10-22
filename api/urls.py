from django.urls import path, include
from .khach_hang.urls import url_khach_hang
from .quan_tri.urls import url_quan_tri

urlpatterns = url_khach_hang + url_quan_tri