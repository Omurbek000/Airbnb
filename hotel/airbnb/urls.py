from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('user/profile/', UserProfileListApiView.as_view(), name='user-profile'),
    path('user/profile/detail/', UserProfileDetailApiView.as_view(), name='user-profile-detail'),
    path('countries/', CountryListApiView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetailApiView.as_view(), name='country-detail'),
    path('cities/', CityListApiView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailApiView.as_view(), name='city-detail'),  
    path('hotels/', HotelListApiView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelDetailApiView.as_view(), name='hotel-detail'),
    path('hotels/create/', HotelCreateApiView.as_view(), name='hotel-create'),
    path('hotels/<int:pk>/edit/', HotelEDITAPIView.as_view(), name='hotel-edit'),
    path('rooms/', RoomListAPIView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room-detail'),
    path('rooms/create/', RoomCreateAPIView.as_view(), name='room-create'),
    path('rooms/<int:pk>/edit/', RoomEDITAPIView.as_view(), name='room-edit'),
]
