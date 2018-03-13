#! -*- coding: utf-8 -*-

import requests
import datetime

import sys
from django.core.management.base import BaseCommand
from game.models import Genre, GameContentType, Platform, Game, Price


class Command(BaseCommand):
    help = 'Update all game in Games table from store.playstation.com'

    def handle(self, *args, **options):
        store_ps_json = 'https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT' \
                        '?platform=ps4&game_content_type=games&size=30&start=%s'
        explude_content_type = [u'', u'Аватар', u'Тема', u'Аватары', u'Демоверсия']

        n = 1
        count_games_and_bundles = (requests.get(store_ps_json % 0)).json()['data']['attributes']['facets'][0]['values']
        games_count = next(i['count'] for i in count_games_and_bundles if i['key'] == 'games')
        for games in range(0, games_count, 30):
            r = requests.get(store_ps_json % games)
            data = r.json()['included']

            if not data:
                self.stderr.write('ERROR: No games to parse')
                sys.exit(status=-1)

            for i in data:
                ps_game_id = i['id']
                i = i['attributes']
                if i.get('genres') and i['game-content-type'] not in explude_content_type:

                    ps_genres = i['genres']  # жанр
                    ps_content_type = i['game-content-type']  # тип игры
                    ps_platforms = i['platforms']
                    ps_name = i['name']
                    ps_release_date = datetime.datetime.strptime(i['release-date'], '%Y-%m-%dT%H:%M:%SZ').date()
                    ps_price_non_plus_user, ps_price_plus_user = None, None
                    if i.get('skus'):
                        ps_price_non_plus_user = i['skus'][0]['prices']['non-plus-user']['actual-price']['value']
                        ps_price_plus_user = i['skus'][0]['prices']['plus-user']['actual-price']['value']
                    ps_rating_score = i['star-rating']['score']
                    ps_rating_people = i['star-rating']['total']
                    ps_page = 'https://store.playstation.com/ru-ru/product/%s' % ps_game_id
                    ps_logo = i['thumbnail-url-base']

                    # generate relative objects set: genres
                    genres = []
                    for g in ps_genres:
                        genre, created = Genre.objects.get_or_create(name=g)
                        genres.append(genre)

                    # game-content-type
                    content_type, created = GameContentType.objects.get_or_create(name=ps_content_type)

                    # generate relative objects set: platforms
                    platforms = []
                    for p in ps_platforms:
                        platform, created = Platform.objects.get_or_create(name=p)
                        platforms.append(platform)

                    # game
                    # Games.objects.update_or_create(
                    #     Q(ps_id=ps_game_id) | Q(name=ps_name),
                    #     defaults={
                    #         'release_date': ps_release_date,
                    #         'genres': genres,
                    #         'content_type': content_type,
                    #         'platforms': platforms,
                    #         'price_non_plus_user': ps_price_non_plus_user,
                    #         'price_plus_user': ps_price_plus_user,
                    #         'rating_score': ps_rating_score,
                    #         'rating_people': ps_rating_people,
                    #         'page': ps_page,
                    #         'logo': ps_logo
                    #     }
                    # )

                    game, created = Game.objects.get_or_create(name=ps_name)
                    game.ps_id = ps_game_id
                    game.release_date = ps_release_date
                    game.genres.add(*genres)
                    game.content_type_id = content_type.id
                    game.platforms.add(*platforms)
                    # game.price_non_plus_user = ps_price_non_plus_user
                    # game.price_plus_user = ps_price_plus_user
                    game.rating_score = ps_rating_score
                    game.rating_people = ps_rating_people
                    game.page = ps_page
                    game.logo = ps_logo
                    game.save()

                    # add price
                    if ps_price_plus_user or ps_price_non_plus_user:
                        Price.objects.create(
                            game=game,
                            price_plus_user=ps_price_plus_user,
                            price_non_plus_user=ps_price_non_plus_user
                        )

                    self.stdout.write(self.style.SUCCESS('Successfully parse game # %s: "%s"' % (n, ps_name)))
                    n += 1
