from django.urls import path
from .views import ReservationCreate, ReservationUpdateDelete
urlpatterns = [
    path('api/bookings/', ReservationCreate.as_view(), name='reservation-create'),
    path('api/bookings/<int:id>/', ReservationUpdateDelete.as_view(), name='reservation-update-delete'),
]




