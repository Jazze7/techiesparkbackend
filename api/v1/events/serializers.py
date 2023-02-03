from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from web.models import Event



class EventSerializer(ModelSerializer):
    date=serializers.DateField(format="%d %b %Y" )
    class Meta:
        fields = "__all__"
        model = Event

    
