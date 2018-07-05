from django.views.generic import ListView

from game.models import Game


class MainPageView(ListView):
    paginate_by = 5
    model = Game
    template_name = 'mainpage.html'

