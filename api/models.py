from django.db import models

class Phim(models.Model):
    ten_phim = models.CharField(max_length=255)
    dao_dien = models.CharField(max_length=100)
    dien_vien = models.CharField(max_length=100)
    the_loai = models.CharField(max_length=100)
    thoi_luong = models.IntegerField()
    mo_ta = models.TextField()
    ngay_phat_hanh = models.DateField()
    image = models.CharField(max_length=255)

class User(models.Model):
    ho_ten = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=20)
    mat_khau = models.CharField(max_length=50)
    vai_tro = models.CharField(max_length=100)
    luong = models.DecimalField(max_digits=15, decimal_places=3)

class Rap(models.Model):
    ten_rap = models.CharField(max_length=255)
    dia_chi = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=20)
    so_phong_chieu = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PhongChieu(models.Model):
    ten_phong = models.CharField(max_length=100)
    so_ghe = models.IntegerField()
    rap = models.ForeignKey(Rap, on_delete=models.CASCADE)

class LichChieu(models.Model):
    thoi_gian = models.TimeField()
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
    phong_chieu = models.ForeignKey(PhongChieu, on_delete=models.CASCADE)

class Ghe(models.Model):
    loai_ghe = models.CharField(max_length=50)
    trang_thai = models.CharField(max_length=10)
    phong_chieu = models.ForeignKey(PhongChieu, on_delete=models.CASCADE)


class Ve(models.Model):
    ngay_dat = models.DateField()
    tong_tien = models.DecimalField(max_digits=15, decimal_places=3)
    phuong_thuc = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    so_ghe = models.CharField(max_length=10)
    lich_chieu = models.ForeignKey(LichChieu, on_delete=models.CASCADE)


