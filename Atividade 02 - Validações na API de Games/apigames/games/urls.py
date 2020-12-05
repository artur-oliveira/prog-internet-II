from django.urls import path
from .views import games_list, games_detail

urlpatterns = [
    path('games/', games_list),
    path('games/<int:pk>', games_detail)
]