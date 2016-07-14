import os
import django
from django.http import JsonResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reddit_gallery.server.config.settings")
django.setup()
from reddit_gallery.server.gallery.models import Images
from reddit_gallery.server.gallery.serializers import ImagesSerializer

def main(): 
    images = Images.objects.all()
    serializer = ImagesSerializer(images)
    #return "hello"
    print serializer.data
    print JsonResponse(serializer.data)

if __name__ == '__main__':
    main()
