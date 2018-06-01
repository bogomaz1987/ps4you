from django.views.generic import ListView

from game.models import Game


class MainPageView(ListView):
    paginate_by = 10
    model = Game
    template_name = 'mainpage.html'

    # def get_context_data(self):
    #     g = Game.objects.all()[:10]
    #     print(dir(g[0]))
    #     return ''
