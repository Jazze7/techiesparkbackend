from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from web.models import Event,MomentGallery


class EventSerializer(ModelSerializer):
    date=serializers.DateField(format="%d %b %Y" )
    gallery=serializers.SerializerMethodField()

    class Meta:
        fields =("id", "title", "description", "image","date", "gallery")
        model = Event

    
    def get_gallery(self,instance):
        request = self.context.get("request")
        image=MomentGallery.objects.filter(title=instance)
        serializer=MomentGallerySerializer(image,many=True,context={"request":request})
        return serializer.data


class MomentGallerySerializer(ModelSerializer):
    class Meta:
        fields = ("id","image")
        model = MomentGallery
        
