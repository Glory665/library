from rest_framework.viewsets import ModelViewSet

from .models import TodoUser
from .serializers import TodoModelSerializer


class TodoModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = TodoUser.objects.all()
    serializer_class = TodoModelSerializer