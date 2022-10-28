from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class YoungAdultFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Young Adult Fiction')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Adventure')
    serializer_class = BookSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Action')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Horror')
    serializer_class = BookSerializer


class SciFiViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Sci-Fi')
    serializer_class = BookSerializer


class ComicBookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Comic Book')
    serializer_class = BookSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Thriller')
    serializer_class = BookSerializer
