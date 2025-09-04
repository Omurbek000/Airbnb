from django.contrib.auth.models import AbstractUser,
from django.db import models  
from phonenumber_field.modelfields import PhoneNumberField,
from django.core.validators import MinValueValidator,MaxValueValidator,


class Country(models.Model):
  country_name = models.CharField(max_length=30, unique=True)
  country_capital = models.CharField(max_length=30, unique=True)
  country_currency = models.CharField(max_length=30, unique=True)
  country_image = models.ImageField(upload_to='country/images')
  
  class Meta:
      verbose_name = 'Страна'
      verbose_name_plural = 'Страны'
  
  def __str__(self):
    return f"{self.country_name}:{self.country_capital}:{self.country_currency}:{self.country_image}"


class UserProfile(AbstractUser):
  ROLE_CHOISES = (
    ('Admin', 'Admin'),
    ('User', 'User'),
    ('Guest', 'Guest'),
  )
  user_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
  user_role = models.CharField(max_length=10, choices=ROLE_CHOISES, default='Guest')
  user_age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
  
  def __str__(self):
    return f"{self.last_name}:{self.first_name}:{self.user_role}"
  
  
class City(models.Model):
    city_name = models.CharField(max_length=100, verbose_name="Название города")
    city_country = models.ForeignKey(Country ,on_delete=models.CASCADE,related_name='cities',verbose_name="Страна" )
    city_capital = models.BooleanField(default=False, verbose_name="Столица страны?", null=True, blank=True)
    
    class Meta:
      verbose_name = "Город"
      verbose_name_plural = "Города"

    def __str__(self):
      return f"{self.city_name}:{self.city_country}:{self.city_capital}"

class Hotel(models.Model)
  pass