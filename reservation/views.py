
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ReservationSerializer

BOOKINGS_STORE = {}

class ReservationCreate(APIView):
    def get(self, request):
        reservations = list(BOOKINGS_STORE.values())
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationUpdateDelete(APIView):
    def get_reservation(self, reservation_id):
        reservation = BOOKINGS_STORE.get(reservation_id)
        return reservation

    def get(self, request, reservation_id):
        reservation = self.get_reservation(reservation_id)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def delete(self, request, reservation_id):
        self.get_reservation(reservation_id)  
        del BOOKINGS_STORE[reservation_id]
        return Response(status=status.HTTP_204_NO_CONTENT)



