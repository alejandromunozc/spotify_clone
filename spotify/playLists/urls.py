"""Play Lists URL's."""

# Django
from django.urls import path

# Views
from spotify.playLists import views


urlpatterns = [
    # Management
    path(
        route='addTrack/<str:title>',
        view=views.add_track,
        name='addTrack'
    ),
    path(
        route='addFavorite/<str:title>',
        view=views.add_favorite_track,
        name='addFavorite'
    ),
]
