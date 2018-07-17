from django.views.generic import ListView

from game.models import Game


class MainPageView(ListView):
    paginate_by = 5
    model = Game
    template_name = 'home.html'
    ordering = ['-rating_people', '-rating_score']

    def get_queryset(self):
        search_word = self.request.GET.get('q', '')
        return Game.objects.filter(name__contains=search_word).order_by(*self.ordering)



