from rest_framework import serializers
from gallery.models import Images

class ImagesSerializer(serializers.ModelSerializer):
    """Serializer to represent the Images model"""
    class Meta:
        model = Images
        field = ("id", "path", "url")
