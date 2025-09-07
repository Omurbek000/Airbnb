from .models import Country, City, Hotel, Room, Review
from modeltranslation.translator import TranslationOptions, register


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'hotel_address')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('rev_text', 'rev_user_name', 'rev_reply')