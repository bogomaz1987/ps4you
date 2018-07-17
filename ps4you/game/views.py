from django.views.generic import DetailView

from game.models import Game


class GameDetailVeiew(DetailView):
    model = Game
    template_name = 'game-detail.html'
