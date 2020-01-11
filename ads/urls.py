from django.urls import path
from .views import *

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
]