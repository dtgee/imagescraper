from rest_framework import viewsets
from gallery.models import Images
from gallery.serializers import ImagesSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Images objects """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

def index(request):
    queryset = Images.objects.all()
    return render(request, 'index.html')
