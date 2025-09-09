from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from tokenize import TokenError



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "username": instance.username,
            "email": instance.email,
        }



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if not user:
            raise serializers.ValidationError("Неверный логин или пароль")
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "username": instance.username,
                "email": instance.email,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def validate(self, data):
        try:
            self.token = RefreshToken(data["refresh"])
        except TokenError:
            raise serializers.ValidationError({"detail": "Неверный или просроченный токен"})
        return data

    def save(self, **kwargs):
        self.token.blacklist()



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name", "country_currency", "country_image"]


class UserProfileSerializer(serializers.ModelSerializer):
    user_country = CountrySerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ["user_country", "user_role", "user_age"]


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "first_name", "last_name"]


class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city_name"]


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ["hotel_image"]


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ["room_image"]


class ReviewSerializer(serializers.ModelSerializer):
    rev_user_name = UserProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["rev_user_name", "rev_text", "rev_stars", "rev_created_at"]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)



class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            "id", "room_name", "room_status", "room_price",
            "room_capacity", "room_type", "room_images",
        ]


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            "id", "room_name", "room_description", "room_status", "room_images"
        ]



class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    hotel_city = CitySimpleSerializer(read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = [
            "id", "hotel_name", "hotel_description", "hotel_address",
            "hotel_images", "hotel_city", "avg_rating", "count_people"
        ]

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class HotelDetailSerializer(serializers.ModelSerializer):
    rooms = RoomListSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    hotel_owner = UserProfileSimpleSerializer(read_only=True)
    hotel_city = CitySimpleSerializer(read_only=True)
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            "hotel_name", "hotel_description", "hotel_address", "hotel_price",
            "hotel_video", "rooms", "hotel_stars", "avg_rating", "count_people",
            "hotel_owner", "hotel_city", "hotel_images", "reviews"
        ]

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class CountryListSerializer(serializers.ModelSerializer):
    cities = CitySimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ["country_name", "cities"]


class CityListSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ["city_name", "hotels"]