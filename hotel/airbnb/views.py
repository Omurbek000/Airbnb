from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import HotelFilter, RoomFilter, BookingFilter
from .paginations import *
from. permissions import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(serializer.to_representation(user), status=status.HTTP_200_OK)



class LogoutView(APIView):

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'detail': 'Токен не найден'}, status=status.HTTP_404_NOT_FOUND)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Успешно вышли из системы'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'detail': 'Неверный или просроченный токен'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileListApiView(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class UserProfileDetailApiView(generics.RetrieveDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CountryListApiView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailApiView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer



class CityListApiView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer


class CityDetailApiView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [permissions.IsAdminUser]

class HotelListApiView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend ,SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    ordering_fields = ['hotel_stars', 'hotel_price']
    search_fields = ['hotel_name', 'hotel_description', 'hotel_address']
    pagination_class = HotelNumberPagination


class HotelDetailApiView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


class HotelCreateApiView(generics.CreateAPIView):
    serializer_class = HotelSerializer
    permission_classes = [CheckCreateHotel]


class HotelEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelSerializer
    permission_classes = [CheckHotelOwner, CheckCreateHotel]

    def get_queryset(self):
        return Hotel.objects.filter(hotel_owner=self.request.user)



class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['room_price']
    search_fields = ['room_name']


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    permission_classes = [CheckCreateHotel]


class RoomEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    permission_classes = [CheckHotelOwner, CheckCreateHotel]

    def get_queryset(self):
        return Room.objects.filter(room_hotel__hotel_owner=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CreateReview]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer