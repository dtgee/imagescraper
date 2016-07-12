from gallery.models import Images
import json

images = Images.objects.all()
serializer = ImagesSerializer(images)
return HttpResponse(json.dumps(serializer))
