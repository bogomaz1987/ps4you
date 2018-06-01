from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('searchableselect/', include('searchableselect.urls')),

    path('', include('page.urls')),
    path('client/', include('client.urls')),
]
