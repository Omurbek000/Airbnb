from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import HotelFilter, RoomFilter, BookingFilter
from .paginations import *
from. permissions import 
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class CustomLoginView(TokenObtainPairView):
  serializer_class = UserLoginSerializer
  
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    try:
      serializer.is_valid(raise_exception=True)
    except Exception:
      return Response({'detail': 'Неверный логин или пароль'}, status=status.HTTP_401_UNAUTHORIZED)
     user = serializer.validated_data 
     return Response(serializer.data, status=status.HTTP_200_OK)


class LogautView(APIView):
  def post(self, request):
    try:
      refresh_token = request.data.get('refresh')
      if refresh_token:
        return Response({'detail': 'Токен не найден'}, status=status.HTTP_404_NOT_FOUND)
       token = RefreshToken("refresh_token")
       token.blacklist()
       return Response({'успешно вышли из системы '}, status=status.HTTP_200_OK)
    except TokenError as e:
      return Response({'detail': 'Неверный или просроченный токен'}, status=status.HTTP_400_BAD_REQUEST)
     