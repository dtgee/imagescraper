from rest_framework import viewsets
from gallery.models import Images
from gallery.serializers import ImagesSerializer
from django.http import JsonResponse

class ImagesViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Images objects """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

def index(request):
    queryset = Images.objects.all()
    return render(request, 'index.html')

def grab_images(request):
    queryset = Images.objects.all()
    serializer = ImagesSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
