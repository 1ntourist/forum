from django.views.generic import ListView, DetailView
from .models import *


class AdsListView(ListView):
    model = Ads
    template_name = 'ads/ads_list.html'
    context_object_name = 'ads_list'
