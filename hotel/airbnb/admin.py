from django.contrib import admin
from .models import Country, City, Hotel, HotelImage, Room, RoomImage, UserProfile, Review, Booking
from modeltranslation.admin import TranslationAdmin



class BaseTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Country, City)
class CountryCityAdmin(BaseTranslationAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(BaseTranslationAdmin):
  pass 

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1



@admin.register(Hotel)
class HotelAdmin(BaseTranslationAdmin):
    inlines = [HotelImageInline]



@admin.register(Room)
class RoomAdmin(BaseTranslationAdmin):
    inlines = [RoomImageInline]



admin.site.register(UserProfile)
admin.site.register(Booking)
