"""CS3620_BookAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from BookAPI.views import BookViewSet, YoungAdultFictionViewSet, FantasyViewSet, AdventureViewSet, ActionViewSet, RomanceViewSet, MysteryViewSet, HorrorViewSet, SciFiViewSet, ComicBookViewSet, ThrillerViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('youngadultfiction', YoungAdultFictionViewSet)
router.register('fantasy', FantasyViewSet)
router.register('adventure', AdventureViewSet)
router.register('action', ActionViewSet)
router.register('romance', RomanceViewSet)
router.register('mystery', MysteryViewSet)
router.register('horror', HorrorViewSet)
router.register('scifi', SciFiViewSet)
router.register('comicbook', ComicBookViewSet)
router.register('thriller', ThrillerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
