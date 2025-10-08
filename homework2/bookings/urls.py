from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('', views.movie_list, name='movie_list'), 
    path('movies/', views.movie_list, name='movie_list'),
    path('seats/', views.seat_booking, name='seat_booking'),
    path('history/', views.booking_history, name='booking_history'),
    path('seats/<int:movie_id>/', views.seat_booking, name='seat_booking'),
    path('login/', auth_views.LoginView.as_view(template_name='bookings/login.html'), name='login'),
]