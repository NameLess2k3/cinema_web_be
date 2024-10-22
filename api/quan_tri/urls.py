from django.urls import path
from .quan_ly_danh_muc import manage_movie, manage_schedule, manage_screening_room, manage_cinema
from .quan_ly_he_thong import login_view,logout_view,update_user_view,roles_view,assign_role_view,update_website_info_view
from .quan_ly_khach_hang import customer_info_view,invoice_management_view,promotion_management_view
from .quan_ly_tai_chinh import revenue_statistics_view,ticket_sales_statistics_view,screening_schedule_statistics_view
from .quan_ly_ve import manage_ticket_info,update_ticket_count,payment_processing

url_quan_tri = [
    path('quan_ly_danh_muc/movie/', manage_movie, name='manage_movie'),
    path('quan_ly_danh_muc/schedule/', manage_schedule, name='manage_schedule'),
    path('quan_ly_danh_muc/screening_room/', manage_screening_room, name='manage_screening_room'),
    path('quan_ly_danh_muc/cinema/', manage_cinema, name='manage_cinema'),

    path('quan_ly_he_thong/login/', login_view, name='login'),
    path('quan_ly_he_thong/logout/', logout_view, name='logout'),
    path('quan_ly_he_thong/user/update/', update_user_view, name='update_user'),
    path('quan_ly_he_thong/roles/', roles_view, name='roles'),
    path('quan_ly_he_thong/assign-role/', assign_role_view, name='assign_role'),
    path('quan_ly_he_thong/website/update/', update_website_info_view, name='update_website_info'),

    path('quan_ly_khach_hang/customer/', customer_info_view, name='customer_info'),
    path('quan_ly_khach_hang/invoice/', invoice_management_view, name='invoice_management'),
    path('quan_ly_khach_hang/promotion/', promotion_management_view, name='promotion_management'),

    path('quan_ly_tai_chinh/revenue/', revenue_statistics_view, name='revenue_statistics'),
    path('quan_ly_tai_chinh/ticket-sales/', ticket_sales_statistics_view, name='ticket_sales_statistics'),
    path('quan_ly_tai_chinh/screening-schedule/', screening_schedule_statistics_view, name='screening_schedule_statistics'),

    path('quan_ly_ve/ticket-info/', manage_ticket_info, name='manage_ticket_info'),
    path('quan_ly_ve/ticket-count/', update_ticket_count, name='update_ticket_count'),
    path('quan_ly_ve/payment/', payment_processing, name='payment_processing'),
]
