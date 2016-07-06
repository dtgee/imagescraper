from rest_framework import viewsets
from gallery.models import Images
from gallery.serializers import ImagesSerializer

class ImagesViewSet(viewsets.ModeViewSet):
    """ ViewSet for viewing and editing Images objects """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
