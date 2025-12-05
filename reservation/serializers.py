from rest_framework import serializers
from .models import Category, Post, Comment
from django.contrib.auth.models import Reservation

"""
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "room", "house", "start_time", "end_time"]        
"""       
        
from rest_framework import serializers

class ReservationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Hogwarts_house = serializers.ChoiceField(
        choices=["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    )
    room = serializers.IntegerField() 
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()        