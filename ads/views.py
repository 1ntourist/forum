from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.forms import ModelForm
from .models import *
from django.urls import reverse, reverse_lazy


class Home(TemplateView): # главная страница
    template_name = 'home.html'


def rubric_list(requests):  # Функция возвращает список главных рубрик
    rubrics = Rubric.objects.all()
    context = {
        'rubrics': rubrics,
    }
    return render(requests, 'rubric/rubric_list.html', context)


def theme_of_rubric(requests, id):   # Функция показывает все темы определенной рубрики
    themes = Theme.objects.all()
    themes = themes.filter(rubric=id)
    context = {
        'themes': themes,
    }
    return render(requests, 'themes/themes.html', context)


class AdsList(ListView):  # Выводит все объявления
    model = Ads
    template_name = 'ads/all_ads.html'
    ordering = '-date'
    context_object_name = 'all_ads'


################################################### C R U D ############################################


def ads_of_themes(request, rubric, theme):  # Функци показывает все обьявления определенной темы и рубрики
    ads = Ads.objects.all()
    ads = ads.filter(rubric=rubric, theme=theme, )
    context = {
        'adss': ads,
    }
    return render(request, 'ads/ads_list.html', context)


def detail_of_theme(requests, rubric, theme, id):   # Функция показывающая все детали обьявления
    ads = Ads.objects.all()
    ads = ads.filter(rubric=rubric, theme=theme, id=id)
    return render(requests, 'ads/ads_detail.html', {'adss': ads})


class AdsForm(ModelForm):   # Форма для создания объявления
    class Meta:
        model = Ads
        fields = '__all__'


def ads_create(request):  # функция создания объявления
    form = AdsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('rubric_list')
    return render(request, 'ads/ads_create.html', {'form': form})
