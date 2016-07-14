import os
import django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reddit_gallery.server.config.settings")
django.setup()
from reddit_gallery.server.gallery.models import Images
from reddit_gallery.server.gallery.serializers import ImagesSerializer

def main(): 
    images = Images.objects.all()
    serializer = ImagesSerializer(images, many=True)
    #print serializer.data
    print json.dumps(serializer.data)

if __name__ == '__main__':
    main()
