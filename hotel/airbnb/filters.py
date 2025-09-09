import django_filters
from .models import Hotel, Room, Booking

class HotelFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="hotel_price",exact='gte')
    price_max = django_filters.NumberFilter(field_name="hotel_price",exact='lte')
    stars_min = django_filters.NumberFilter(field_name="hotel_stars",exact='gte')
    stars_max = django_filters.NumberFilter(field_name="hotel_stars",exact='lte')

    class Meta:
        model = Hotel
        fields = ['hotel_city', 'hotel_stars', 'hotel_price']


class RoomFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="room_price",exact='gte')
    price_max = django_filters.NumberFilter(field_name="room_price",exact='lte')
    capacity_min = django_filters.NumberFilter(field_name="room_capacity",exact='gte')
    capacity_max = django_filters.NumberFilter(field_name="room_capacity",exact='lte')

    class Meta:
        model = Room
        fields = ['room_hotel', 'room_status', 'room_capacity', 'room_price']


class BookingFilter(django_filters.FilterSet):
    check_in_after = django_filters.DateFilter(field_name="check_in", expr='gte')
    check_in_before = django_filters.DateFilter(field_name="check_in",exact='lte')
    price_min = django_filters.NumberFilter(field_name="total_price",exact='gte')
    price_max = django_filters.NumberFilter(field_name="total_price",exact='lte')

    class Meta:
        model = Booking
        fields = ['hotel_book', 'room_book', 'user_book', 'status_book',]
