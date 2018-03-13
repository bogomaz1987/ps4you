https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?platform=ps4&bucket=games
https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?size=30&bucket=games&start=0
https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?size=30&bucket=games&start=30
https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?size=30&bucket=games&start=60
https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?size=30&bucket=games&start=90
https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?platform=ps4&game_content_type=games&size=30&bucket=games&start=0
https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?size=30&bucket=games&start=720


attributes
    genres
    game-content-type
    name
    platforms


import requests
n=0
r = requests.get('https://store.playstation.com/valkyrie-api/ru/RU/19/container/STORE-MSF75508-PS4CAT?platform=ps4&game_content_type=games&size=30&start=%s' % n)
a = r.json()['included']
for i in a:
    if i['attributes'].get('genres') and i['attributes']['game-content-type'] not in [u'', u'Аватар', u'Тема', u'Аватары', u'Демоверсия']:
        
        print [x for x in i['attributes']['genres']]
        print i['attributes']['game-content-type']
        print [x for x in i['attributes']['platforms']]
        print i['attributes']['name']
        print i['attributes']['release-date']
        print i['attributes']['skus'][0]['prices']['non-plus-user']['actual-price']['value'], i['attributes']['skus'][0]['prices']['plus-user']['actual-price']['value'], i['attributes']['star-rating']
        print i['attributes']['thumbnail-url-base']
        print 'https://store.playstation.com/ru-ru/product/%s' % i['attributes']['default-sku-id']
        print ''

