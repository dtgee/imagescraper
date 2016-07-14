import os
import django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reddit_gallery.server.config.settings")
django.setup()
from reddit_gallery.server.gallery.models import Images
from reddit_gallery.server.gallery.serializers import ImagesSerializer

def main(): 
    images = Images.objects.all()
    serializer = ImagesSerializer(images)
    #return "hello"
    print HttpResponse(json.dumps(serializer))

if __name__ == '__main__':
    main()
