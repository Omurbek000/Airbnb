from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator



class Country(models.Model):
    country_name = models.CharField(max_length=30, unique=True, verbose_name="Название страны")
    country_capital = models.CharField(max_length=30, unique=True, verbose_name="Столица")
    country_currency = models.CharField(max_length=30, unique=True, verbose_name="Валюта")
    country_image = models.ImageField(upload_to='country/images', blank=True, null=True, verbose_name="Флаг/Фото")

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country_name



class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Администратор'),
        ('User', 'Пользователь'),
        ('Guest', 'Гость'),
    )
    user_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Страна")
    user_role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Guest', verbose_name="Роль")
    user_age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True, verbose_name="Возраст")
    user_phone = PhoneNumberField(region='KG', null=True, blank=True, verbose_name="Телефон")

    def __str__(self):
        return f"{self.username} ({self.user_role})"



class City(models.Model):
    city_name = models.CharField(max_length=100, verbose_name="Название города")
    city_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name="Страна")
    city_capital = models.BooleanField(default=False, verbose_name="Столица страны?")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return f"{self.city_name}, {self.city_country.country_name}"



class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name="Название отеля")
    hotel_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels', verbose_name="Город")
    hotel_owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='hotels', null=True, blank=True, verbose_name="Владелец")
    hotel_phone = PhoneNumberField(region='KG', null=True, blank=True, verbose_name="Телефон")
    hotel_description = models.TextField(max_length=1000, verbose_name="Описание отеля")
    hotel_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Количество звёзд")
    hotel_address = models.CharField(max_length=100, verbose_name="Адрес отеля")
    hotel_create_date = models.DateTimeField(auto_now_add=True)
    hotel_update_date = models.DateTimeField(auto_now=True)
    hotel_video = models.FileField(upload_to='hotel/video', null=True, blank=True, verbose_name="Видео")
    hotel_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за ночь")

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"

    def __str__(self):
        return f'{self.hotel_name} ({self.hotel_city.city_name})'

    def get_avg_rating(self):
        rating = self.reviews.all()
        if rating.exists():
            return round(sum([i.rev_stars for i in rating]) / rating.count(), 2)
        return 0

    def get_count_people(self):
        return self.reviews.count()


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images', verbose_name="Отель")
    hotel_image = models.ImageField(upload_to='hotel_images/', null=True, blank=True, verbose_name="Фото")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"Фото {self.hotel_image} {self.hotel_name}"



class Room(models.Model):
    room_name = models.CharField(max_length=100, verbose_name="Название комнаты")
    room_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms', verbose_name="Отель")

    TYPE_ROOM = (
        ('single', 'Одноместный'),
        ('double', 'Двухместный'),
        ('suite', 'Люкс'),
        ('family', 'Семейный'),
    )
    room_type = models.CharField(max_length=16, choices=TYPE_ROOM, verbose_name="Тип комнаты")

    STATUS_CHOICES = (
        ('свободен', 'Свободен'),
        ('забронирован', 'Забронирован'),
        ('занят', 'Занят'),
    )
    room_status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name="Статус комнаты")
    room_available = models.BooleanField(default=True, verbose_name="Доступна для брони?")
    room_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за ночь")
    room_description = models.TextField(max_length=1000, verbose_name="Описание комнаты")
    room_capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Вместимость")
    room_bed_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Количество кроватей")

    def __str__(self):
        return f"{self.room_name} ({self.room_hotel})"



class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images', verbose_name="Комната")
    room_image = models.ImageField(upload_to='room_images/', null=True, blank=True, verbose_name="Фото комнаты")

    def __str__(self):
        return f"Фото {self.room_image} "



class Review(models.Model):
    rev_user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
    rev_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews', verbose_name="Отель")
    rev_text = models.TextField(verbose_name="Текст отзыва")
    rev_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True, verbose_name="Оценка")
    rev_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rev_updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    rev_is_published = models.BooleanField(default=True, verbose_name="Опубликован?")
    rev_reply = models.TextField(blank=True, null=True, verbose_name="Ответ администрации")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-rev_created_at']

    def __str__(self):
        return f"{self.rev_user_name} {self.rev_hotel} {self.rev_stars}"



class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Номер")
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
    check_in = models.DateTimeField(verbose_name="Дата заезда")
    check_out = models.DateTimeField(verbose_name="Дата выезда")
    guests_count = models.PositiveSmallIntegerField(default=1, verbose_name="Количество гостей")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Итоговая цена")

    STATUS_BOOK_CHOICES = (
        ('отменено', 'Отменено'),
        ('подтверждено', 'Подтверждено'),
        ('ожидает', 'Ожидает подтверждения'),
    )
    status_book = models.CharField(max_length=20, choices=STATUS_BOOK_CHOICES, default='ожидает', verbose_name="Статус брони")

    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('не оплачено', 'Не оплачено'),
            ('оплачено', 'Оплачено'),
            ('возврат', 'Возврат'),
        ],
        default='не оплачено',
        verbose_name="Статус оплаты"
    )

    special_requests = models.TextField(blank=True, null=True, verbose_name="Пожелания и специальные запросы")