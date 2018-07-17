from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('searchableselect/', include('searchableselect.urls')),

    path('', include('page.urls')),
    path('game/', include('game.urls')),
    path('client/', include('client.urls')),

    path('auth/', include('social_django.urls', namespace='social'))
]
