from django.urls import path

from page.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
]
