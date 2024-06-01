from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Publication
from .serializers import PublicationSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PublicationList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

