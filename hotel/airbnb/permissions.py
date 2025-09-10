from rest_framework import permissions


class CheckCreateHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_role == 'ownerUser':
                return True
        return False



class CheckHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if hasattr(obj, 'hotel_owner'):
                return obj.hotel_owner == request.user
            if hasattr(obj, 'room_hotel'):
                return obj.room_hotel.hotel_owner == request.user
        return False



class CreateReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_role == 'User':
                return True
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False