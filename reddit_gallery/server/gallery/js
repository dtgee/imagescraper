import os
import django
from django.http import JsonResponse
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reddit_gallery.server.config.settings")
django.setup()
from reddit_gallery.server.gallery.models import Images
from reddit_gallery.server.gallery.serializers import ImagesSerializer

def main(): 
    images = Images.objects.all()
    serializer = ImagesSerializer(images, many=True)
    print json.dumps(serializer.data)
    return JsonResponse(serializer.data, safe=False)

if __name__ == '__main__':
    main()
