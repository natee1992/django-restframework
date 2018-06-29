from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Music
from .serializers import MusicSerializers


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializers
    permission_classes = (IsAuthenticated,)
