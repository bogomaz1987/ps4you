from django.urls import path

from game.views import GameDetailVeiew

urlpatterns = [
    path('<int:pk>/', GameDetailVeiew.as_view(), name='game-detail'),
]